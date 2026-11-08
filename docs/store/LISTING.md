# FocusSmith: Chrome Web Store listing

Copy each block into the matching field of the Chrome Web Store developer dashboard.
The Edge Add-ons listing uses the same text.

---

## Store listing tab

**Name** (from the manifest)

```
FocusSmith
```

**Summary** (from the manifest, 132 characters max)

```
Block distracting sites during focus sessions of any length, and see your focus stats and AI insights on your dashboard.
```

**Description**

```
FocusSmith helps you protect your focus. Start a focus session of any length, and the sites that pull you away stay closed until the timer ends. Then see how your week went on your dashboard, and ask the Focus Coach what to change.

FOCUS SESSIONS OF ANY LENGTH
• Pick 15, 25, 45, 60 or 90 minutes, or type any length up to 4 hours
• Add 5 minutes when you are on a roll
• Time left shows on the toolbar icon
• A notification tells you when the session ends

BLOCK DISTRACTING SITES
• Choose the sites that distract you, like YouTube, Reddit or X
• Block them only during focus sessions, or all the time
• Switch modes from the popup, and see at a glance whether your sites are blocked right now

YOUR DASHBOARD
• Focus time and sessions for today and the last 7 days
• Which blocked sites you tried to open, and how often
• A one-click AI summary of your day, with a practical tip for tomorrow

FOCUS COACH (AI)
• Ask questions like "How did my focus go this week?" and get answers from your own data
• Ask it to block a site, and it prepares the change for you
• Nothing changes until you press Confirm
• Free for 5 questions a day

PRIVATE BY DESIGN
• FocusSmith does not record your browsing history
• The extension checks each page against your blocked list on your own computer
• It only sends your session times and the blocked sites you tried to open, so your dashboard can show them
• No ads, and your data is never sold
• Delete your account and all its data at any time from Settings

GETTING STARTED
1. Install FocusSmith. A short setup page opens.
2. Create a free account at focussmith.com and copy your key from Settings.
3. Paste the key, add the sites you want to block, and start your first session.

The timer works without an account. Choosing sites to block, your stats and the Focus Coach need a free account.

Works in Chrome and other Chromium browsers, such as Edge and Brave.

Questions or feedback: focussmith.app@gmail.com
Privacy policy: https://focussmith.com/privacy
```

**Category:** Productivity → Workflow & Planning
**Language:** English

**Graphic assets** (all in this folder)

| Field | File |
|---|---|
| Store icon (128×128) | `extension/icons/icon128.png` |
| Screenshots (1280×800), in this order | `1-timer.png`, `2-blocked.png`, `3-dashboard.png`, `4-coach.png`, `5-setup.png` |
| Small promo tile (440×280) | `promo-small-440x280.png` |
| Marquee promo tile (1400×560) | `marquee-1400x560.png` |

**Additional fields**

| Field | Value |
|---|---|
| Official URL | `https://focussmith.com` (needs the domain verified in Google Search Console; leave as "None" until then) |
| Homepage URL | `https://focussmith.com` |
| Support URL | `https://github.com/srinivasthomala/focussmith/issues` |
| Mature content | No |

---

## Privacy tab

**Single purpose description**

```
FocusSmith helps people stay focused: it runs focus sessions of any length and blocks the distracting websites the user chooses during those sessions, and shows the user their own focus statistics on a dashboard.
```

**Permission justifications**

`storage`
```
Saves the user's blocked sites, blocking mode, focus timer state, account key and session records that are waiting to sync, so they persist when the browser restarts.
```

`tabs`
```
Reads the address of a tab when it navigates, so the extension can check it against the user's blocked list and show the FocusSmith "Site blocked" page instead of a blocked site. Addresses of sites that are not on the list are not stored or sent anywhere.
```

`alarms`
```
Ends focus sessions on time, updates the minutes-left badge on the toolbar icon, and periodically syncs blocked sites and session records with the user's FocusSmith account.
```

`notifications`
```
Shows one notification when a focus session ends, so the user knows they can take a break.
```

Host permission `https://api.focussmith.com/*`
```
This is FocusSmith's own server. The extension uses it to download the user's blocked sites and to upload their session times and blocked attempts to their dashboard. The extension does not access any other website's content.
```

**Are you using remote code?** No. All JavaScript is included in the extension package.

**Data usage: what the extension collects**

| Data type | Tick? | Why |
|---|---|---|
| Personally identifiable information | ✅ | The account email is shown in the popup ("Connected as ...") |
| Health information | ❌ | |
| Financial and payment information | ❌ | |
| Authentication information | ✅ | The FocusSmith account key the user pastes in |
| Personal communications | ❌ | |
| Location | ❌ | |
| Web history | ✅ | Addresses and times of blocked sites the user tried to open |
| User activity | ❌ | |
| Website content | ❌ | |

**Certify all three:**
- I do not sell or transfer user data to third parties, outside of the approved use cases
- I do not use or transfer user data for purposes that are unrelated to my item's single purpose
- I do not use or transfer user data to determine creditworthiness or for lending purposes

**Privacy policy URL**

```
https://focussmith.com/privacy
```

---

## Distribution tab

- **Payments:** Free of charge
- **Visibility:** Public
- **Regions:** All regions

---

## Test instructions tab (for the reviewer)

```
1. Install the extension. A setup page opens.
2. Create a free account at https://focussmith.com/login?mode=signup (any email works; no confirmation email is needed).
3. On the Settings page, add youtube.com under Blocked sites, then click "Generate key" under API Keys and copy the key.
4. Back on the extension's setup page, paste the key and click Connect. It shows "Connected as <your email>".
5. Open the extension popup, pick 15 minutes (or type 1) and click Start.
6. Open https://www.youtube.com. The FocusSmith "Site blocked" page appears instead.
7. Open https://focussmith.com/dashboard to see the session and the blocked attempt.

The timer also works without an account; blocking needs a list of sites, which is managed from the dashboard.
```
