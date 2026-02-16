/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Bitter', 'serif'],
      },
      colors: {
        // Global Theme Tokens
        primary: 'rgb(var(--color-primary) / <alpha-value>)',
        'primary-fg': 'rgb(var(--color-primary-fg) / <alpha-value>)',
        background: 'rgb(var(--color-background) / <alpha-value>)',
        surface: 'rgb(var(--color-surface) / <alpha-value>)',
        text: 'rgb(var(--color-text-main) / <alpha-value>)',
        muted: 'rgb(var(--color-text-muted) / <alpha-value>)',
        border: 'rgb(var(--color-border) / <alpha-value>)',

        amber: {
          50: '#fffbeb',
          100: '#fef3c7',
          200: '#fde68a',
          300: '#fcd34d',
          400: '#fbbf24',
          500: '#f59e0b', // Honey
          600: '#d97706', // Dark Amber
          700: '#b45309',
          800: '#92400e',
          900: '#78350f',
        },
        forest: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d', // Forest Green
          800: '#166534',
          900: '#14532d',
        },
        stone: {
          850: '#1c1917',
        },
        cream: '#FFFBEB',
        warm: '#FEF3C7',
      },
      boxShadow: {
        'warm': '0 4px 6px -1px rgba(120, 53, 15, 0.1), 0 2px 4px -1px rgba(120, 53, 15, 0.06)',
        'warm-lg': '0 10px 15px -3px rgba(120, 53, 15, 0.1), 0 4px 6px -2px rgba(120, 53, 15, 0.05)',
      }
    },
  },
  plugins: [],
}
