import { nextui } from '@nextui-org/theme'
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/@nextui-org/theme/dist/components/(accordion|avatar|button|card|input|navbar|divider|ripple|spinner).js"
  ],
  theme: {
    extend: {
      colors: {
        'text-muted': 'rgba(var(--text-muted))',
        'primary-accent': 'rgba(var(--primary-accent))',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [
    nextui({
      themes: {
        light: {
          colors: {
            background: '#eceaf5',
            primary: {
              DEFAULT: '#0245EF',
              foreground: '#ffffff',
            },
            secondary: {
              DEFAULT: '#e900e1',
              foreground: '#ffe9fe',
            },
            foreground: '#000000',
            divider: '#666666',
            overlay: '#ffffff',
            content1: '#ffffff',
          },
        },
      },
    }),
  ],
}
export default config
