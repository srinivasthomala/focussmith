import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

const description =
  'FocusSmith blocks distracting sites during focus sessions of any length, tracks your focus time and gives you an AI coach. Free Chrome extension.';

export const metadata: Metadata = {
  metadataBase: new URL('https://focussmith.com'),
  title: 'FocusSmith: block distractions, focus longer',
  description,
  openGraph: {
    title: 'FocusSmith: block distractions, focus longer',
    description,
    url: '/',
    siteName: 'FocusSmith',
    images: [{ url: '/screenshots/dashboard.png', width: 2850, height: 3129 }],
    type: 'website',
  },
  twitter: { card: 'summary_large_image' },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className={inter.className}>{children}</body>
    </html>
  );
}


