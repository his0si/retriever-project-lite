import type { Metadata } from 'next'
import './globals.css'
import Providers from './providers';

export const metadata: Metadata = {
  title: 'Retriever Project - 학교 정보 챗봇',
  description: 'your personal pup-assistant that fetches all school info and sniffs out the perfect match for you.',
  icons: {
    icon: '/images/logo_black.png',
    shortcut: '/images/logo_black.png',
    apple: '/images/logo_black.png',
  },
  manifest: '/manifest.json',
  themeColor: '#000000',
  viewport: 'width=device-width, initial-scale=1, maximum-scale=5',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'default',
    title: 'Retriever',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko" suppressHydrationWarning>
      <head>
        <link rel="manifest" href="/manifest.json" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="default" />
        <meta name="apple-mobile-web-app-title" content="Retriever" />
        <link rel="apple-touch-icon" href="/icons/icon-192x192.png" />
        <meta name="mobile-web-app-capable" content="yes" />
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  const darkMode = localStorage.getItem('darkMode');
                  if (darkMode === 'true' || (!darkMode && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                    document.documentElement.classList.add('dark');
                  }
                } catch (e) {}
              })();
              
              if ('serviceWorker' in navigator) {
                window.addEventListener('load', function() {
                  navigator.serviceWorker.register('/service-worker.js').then(
                    function(registration) {
                      console.log('Service Worker 등록 성공:', registration.scope);
                    },
                    function(err) {
                      console.log('Service Worker 등록 실패:', err);
                    }
                  );
                });
              }
            `,
          }}
        />
      </head>
      <body className="h-full bg-white dark:bg-gray-900 transition-colors duration-200">
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  )
}