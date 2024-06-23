import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Providers from './providers'
import SideBar from '@/components/Layouts/SideBar/SideBar'
import Navigation from '@/components/Layouts/Navigation'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Hirasys',
  description: 'Streamlined Hiring Process',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body
        className={`${inter.className} light bg-background text-foreground`}
      >
        <Providers>
          <div className="flex w-full">
            <SideBar />
            <div className="flex-grow">
              <Navigation />
              <div className='m-10'>{children}</div>
            </div>
          </div>
        </Providers>
      </body>
    </html>
  )
}
