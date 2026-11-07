'use client';

import { useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { createClient } from '@/lib/supabase/client';

interface Account {
  email: string;
  name: string | null;
  avatarUrl: string | null;
  provider: string | null;
}

export function Nav() {
  const pathname = usePathname();
  const router = useRouter();
  const [account, setAccount] = useState<Account | null>(null);
  const [menuOpen, setMenuOpen] = useState(false);
  const [avatarFailed, setAvatarFailed] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  // Who is signed in, so people with more than one account can tell.
  useEffect(() => {
    createClient()
      .auth.getUser()
      .then(({ data: { user } }) => {
        if (!user) return;
        const meta = user.user_metadata || {};
        setAccount({
          email: user.email || '',
          name: meta.full_name || meta.name || null,
          avatarUrl: meta.avatar_url || meta.picture || null,
          provider: user.app_metadata?.provider || null,
        });
      })
      .catch(() => {});
  }, []);

  // Close the menu on an outside click or Escape.
  useEffect(() => {
    if (!menuOpen) return;
    const onClick = (e: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(e.target as Node)) setMenuOpen(false);
    };
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && setMenuOpen(false);
    document.addEventListener('mousedown', onClick);
    document.addEventListener('keydown', onKey);
    return () => {
      document.removeEventListener('mousedown', onClick);
      document.removeEventListener('keydown', onKey);
    };
  }, [menuOpen]);

  const signOut = async () => {
    await createClient().auth.signOut();
    router.push('/login');
    router.refresh();
  };

  const linkClass = (href: string) =>
    pathname === href
      ? 'text-foreground hover:text-primary transition-colors'
      : 'text-muted-foreground hover:text-foreground transition-colors';

  const label = account?.name || account?.email || '';
  const initial = (label || '?').trim().charAt(0).toUpperCase();

  const avatar = (size: string) =>
    account?.avatarUrl && !avatarFailed ? (
      // eslint-disable-next-line @next/next/no-img-element
      <img
        src={account.avatarUrl}
        alt=""
        referrerPolicy="no-referrer"
        onError={() => setAvatarFailed(true)}
        className={`${size} rounded-full object-cover`}
      />
    ) : (
      <span
        className={`${size} inline-flex items-center justify-center rounded-full bg-primary text-sm font-bold text-primary-foreground`}
      >
        {initial}
      </span>
    );

  return (
    <nav className="border-b border-border">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <Link href="/" className="text-xl font-bold text-primary">
            FocusSmith
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/dashboard" className={linkClass('/dashboard')}>
              Dashboard
            </Link>
            <Link href="/settings" className={linkClass('/settings')}>
              Settings
            </Link>

            <div className="relative" ref={menuRef}>
              <button
                onClick={() => setMenuOpen((v) => !v)}
                aria-haspopup="menu"
                aria-expanded={menuOpen}
                title={account ? `Signed in as ${account.email}` : 'Account'}
                className="flex items-center gap-2 rounded-full border border-border py-1 pl-1 pr-3 hover:bg-secondary transition-colors"
              >
                {avatar('h-7 w-7')}
                <span className="hidden max-w-[180px] truncate text-sm sm:inline">
                  {account ? label : 'Account'}
                </span>
                <span className="text-xs text-muted-foreground">▾</span>
              </button>

              {menuOpen && (
                <div
                  role="menu"
                  className="absolute right-0 z-40 mt-2 w-72 rounded-lg border border-border bg-card p-2 shadow-xl shadow-black/40"
                >
                  <div className="flex items-center gap-3 px-2 py-2">
                    {avatar('h-10 w-10 shrink-0')}
                    <div className="min-w-0">
                      <div className="text-xs text-muted-foreground">Signed in as</div>
                      {account?.name && <div className="truncate text-sm font-semibold">{account.name}</div>}
                      <div className="truncate text-sm">{account?.email}</div>
                      {account?.provider && (
                        <div className="text-xs text-muted-foreground">
                          via {account.provider === 'google' ? 'Google' : 'email and password'}
                        </div>
                      )}
                    </div>
                  </div>
                  <div className="my-1 border-t border-border" />
                  <Link
                    href="/settings"
                    role="menuitem"
                    onClick={() => setMenuOpen(false)}
                    className="block rounded-md px-2 py-2 text-sm hover:bg-secondary"
                  >
                    Settings
                  </Link>
                  <button
                    role="menuitem"
                    onClick={signOut}
                    className="block w-full rounded-md px-2 py-2 text-left text-sm hover:bg-secondary"
                  >
                    Sign out
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}
