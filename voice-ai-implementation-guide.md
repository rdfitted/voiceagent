# Voice AI Assistant - Fitted Automation Brand Implementation Guide

## Overview
This guide provides specific implementation steps to apply Fitted Automation's brand guidelines to your Voice AI Assistant boilerplate, including Tailwind CSS configurations, component updates, and styling patterns.

---

## 1. Tailwind CSS Configuration

### Update `tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Fitted Automation Brand Colors
        'fitted': {
          'navy': '#0B213E',
          'blue': '#0074FF', 
          'slate': '#0F172A',
          'gray-text': '#313131',
        },
        // Override default background/foreground
        'background': '#0B213E',
        'foreground': '#FFFFFF',
        'primary': {
          DEFAULT: '#0074FF',
          foreground: '#FFFFFF',
        },
        'secondary': {
          DEFAULT: '#0F172A',
          foreground: '#FFFFFF',
        },
        'muted': {
          DEFAULT: '#313131',
          foreground: '#FFFFFF',
        },
      },
      fontFamily: {
        'poppins': ['Poppins', 'system-ui', 'sans-serif'],
        'roboto': ['Roboto', 'system-ui', 'sans-serif'],
        'sans': ['Poppins', 'system-ui', 'sans-serif'], // Set Poppins as default
      },
      fontSize: {
        'hero': ['180px', { lineHeight: '1.1', letterSpacing: '-0.02em' }],
        'display': ['64px', { lineHeight: '1.2', letterSpacing: '-0.01em' }],
        'heading-1': ['45px', { lineHeight: '1.3' }],
        'heading-2': ['36px', { lineHeight: '1.4' }],
        'heading-3': ['32px', { lineHeight: '1.4' }],
        'heading-4': ['30px', { lineHeight: '1.5' }],
        'body-large': ['27px', { lineHeight: '1.6' }],
        'body': ['24px', { lineHeight: '1.6' }],
        'ui': ['26px', { lineHeight: '1.5' }],
      },
      fontWeight: {
        'regular': '400',
        'medium': '500',
        'semibold': '600',
      },
      spacing: {
        '18': '4.5rem',  // 72px
        '22': '5.5rem',  // 88px
        '26': '6.5rem',  // 104px
        '30': '7.5rem',  // 120px
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-slow': 'pulse 3s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
```

### CSS Variables for Global Styles

Create or update `globals.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Roboto:wght@600&display=swap');

:root {
  /* Fitted Automation Brand Colors */
  --fitted-navy: #0B213E;
  --fitted-blue: #0074FF;
  --fitted-slate: #0F172A;
  --fitted-gray-text: #313131;
  
  /* CSS Variables for consistency */
  --background-primary: var(--fitted-navy);
  --background-secondary: var(--fitted-slate);
  --text-primary: #FFFFFF;
  --text-secondary: var(--fitted-gray-text);
  --accent-primary: var(--fitted-blue);
  
  /* Animation easing */
  --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
}

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html {
  scroll-behavior: smooth;
  font-feature-settings: 'cv11', 'ss01';
  font-variant: normal;
}

body {
  font-family: 'Poppins', system-ui, sans-serif;
  background-color: var(--background-primary);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Font loading optimization */
.fonts-loading {
  visibility: hidden;
}

.fonts-loaded {
  visibility: visible;
}

/* Custom animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 2. Component Styling Updates

### Main Layout Component

```tsx
// app/layout.tsx or similar
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <head>
        <link 
          rel="preload" 
          href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Roboto:wght@600&display=swap" 
          as="style"
        />
      </head>
      <body className="min-h-screen bg-fitted-navy text-white font-poppins antialiased">
        <div className="min-h-screen flex flex-col">
          {children}
        </div>
      </body>
    </html>
  )
}
```

### Header/Navigation Component

```tsx
// components/Header.tsx
export function Header() {
  return (
    <header className="bg-fitted-navy border-b border-fitted-slate/20 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <h1 className="text-heading-4 font-semibold text-white">
              Voice AI Assistant
            </h1>
          </div>
          
          <nav className="hidden md:flex items-center space-x-8">
            <a 
              href="#features" 
              className="text-body font-regular text-white hover:text-fitted-blue transition-colors duration-200"
            >
              Features
            </a>
            <a 
              href="#demo" 
              className="text-body font-regular text-white hover:text-fitted-blue transition-colors duration-200"
            >
              Demo
            </a>
          </nav>
          
          <button className="inline-flex items-center px-6 py-3 border border-fitted-blue bg-fitted-blue hover:bg-blue-600 text-white font-medium rounded-lg transition-all duration-200 hover:-translate-y-0.5">
            Get Started
          </button>
        </div>
      </div>
    </header>
  )
}
```

### Hero Section Component

```tsx
// components/Hero.tsx
export function Hero() {
  return (
    <section className="relative bg-fitted-navy py-20 lg:py-32">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-display lg:text-hero font-semibold text-white mb-8 animate-fade-in">
            AI-Powered Voice Assistant
          </h1>
          <p className="text-body-large text-white/80 max-w-3xl mx-auto mb-12 animate-slide-up">
            Experience the future of voice interaction with our cutting-edge AI technology. 
            Seamless, intelligent, and built for performance.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 animate-slide-up">
            <button className="inline-flex items-center px-8 py-4 bg-fitted-blue hover:bg-blue-600 text-white font-medium rounded-lg transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
              Start Voice Demo
            </button>
            <button className="inline-flex items-center px-8 py-4 border border-white/20 text-white hover:bg-white/10 font-medium rounded-lg transition-all duration-200">
              Learn More
            </button>
          </div>
        </div>
      </div>
      
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-b from-fitted-navy via-fitted-slate to-fitted-navy opacity-50 pointer-events-none" />
    </section>
  )
}
```

### Voice Interface Component

```tsx
// components/VoiceInterface.tsx
import { useState } from 'react'

export function VoiceInterface() {
  const [isListening, setIsListening] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)

  return (
    <div className="bg-fitted-slate rounded-xl p-8 shadow-2xl border border-white/10">
      <div className="text-center">
        <h3 className="text-heading-2 font-semibold text-white mb-6">
          Voice AI Assistant
        </h3>
        
        {/* Voice Visualization */}
        <div className="relative w-32 h-32 mx-auto mb-8">
          <div className={`absolute inset-0 rounded-full border-4 border-fitted-blue ${isListening ? 'animate-pulse-slow' : ''}`}>
            <div className="w-full h-full rounded-full bg-fitted-blue/20 flex items-center justify-center">
              <div className={`w-16 h-16 rounded-full bg-fitted-blue ${isListening ? 'animate-pulse' : ''}`} />
            </div>
          </div>
        </div>
        
        {/* Status Text */}
        <p className="text-body text-white/80 mb-8">
          {isProcessing ? 'Processing your request...' : 
           isListening ? 'Listening...' : 
           'Click to start speaking'}
        </p>
        
        {/* Control Button */}
        <button
          onClick={() => setIsListening(!isListening)}
          className="inline-flex items-center px-8 py-4 bg-fitted-blue hover:bg-blue-600 text-white font-medium rounded-lg transition-all duration-200 hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed"
          disabled={isProcessing}
        >
          {isListening ? 'Stop Listening' : 'Start Voice Chat'}
        </button>
      </div>
    </div>
  )
}
```

### Feature Cards Component

```tsx
// components/FeatureCard.tsx
interface FeatureCardProps {
  icon: React.ReactNode
  title: string
  description: string
}

export function FeatureCard({ icon, title, description }: FeatureCardProps) {
  return (
    <div className="bg-fitted-slate rounded-xl p-6 border border-white/10 hover:border-fitted-blue/50 transition-all duration-300 hover:-translate-y-1">
      <div className="w-12 h-12 bg-fitted-blue/20 rounded-lg flex items-center justify-center mb-4 text-fitted-blue">
        {icon}
      </div>
      <h3 className="text-heading-3 font-semibold text-white mb-3">
        {title}
      </h3>
      <p className="text-body text-white/70 leading-relaxed">
        {description}
      </p>
    </div>
  )
}

// Usage example
export function Features() {
  const features = [
    {
      icon: <MicrophoneIcon className="w-6 h-6" />,
      title: "Natural Voice Recognition",
      description: "Advanced speech-to-text processing with industry-leading accuracy and real-time response."
    },
    {
      icon: <BrainIcon className="w-6 h-6" />,
      title: "Intelligent Processing",
      description: "Powered by cutting-edge AI models for context-aware conversations and smart responses."
    },
    {
      icon: <SpeakerIcon className="w-6 h-6" />,
      title: "High-Quality Voice Synthesis",
      description: "Natural-sounding text-to-speech with multiple voice options and emotional expression."
    }
  ]

  return (
    <section className="py-20 bg-fitted-navy">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-heading-1 font-semibold text-white mb-6">
            Powerful Voice AI Features
          </h2>
          <p className="text-body-large text-white/80 max-w-2xl mx-auto">
            Experience next-generation voice technology with our comprehensive AI assistant platform.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <FeatureCard key={index} {...feature} />
          ))}
        </div>
      </div>
    </section>
  )
}
```

---

## 3. Utility Classes and Helpers

### Custom CSS Classes

```css
/* Add to globals.css */

/* Button Components */
.btn-primary {
  @apply inline-flex items-center px-6 py-3 bg-fitted-blue hover:bg-blue-600 text-white font-medium rounded-lg transition-all duration-200 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-fitted-blue focus:ring-offset-2 focus:ring-offset-fitted-navy;
}

.btn-secondary {
  @apply inline-flex items-center px-6 py-3 border border-white/20 text-white hover:bg-white/10 font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-white/20;
}

/* Card Components */
.card-fitted {
  @apply bg-fitted-slate rounded-xl p-6 border border-white/10 hover:border-fitted-blue/50 transition-all duration-300;
}

.card-fitted-hover {
  @apply card-fitted hover:-translate-y-1;
}

/* Text Styles */
.text-gradient {
  @apply bg-gradient-to-r from-fitted-blue to-blue-400 bg-clip-text text-transparent;
}

/* Focus States */
.focus-fitted {
  @apply focus:outline-none focus:ring-2 focus:ring-fitted-blue focus:ring-offset-2 focus:ring-offset-fitted-navy;
}
```

---

## 4. Performance Optimizations

### Font Loading Strategy

```tsx
// components/FontLoader.tsx
"use client"

import { useEffect } from 'react'

export function FontLoader() {
  useEffect(() => {
    // Add font loading class
    document.documentElement.classList.add('fonts-loading')
    
    // Load fonts
    const loadFonts = async () => {
      try {
        await Promise.all([
          document.fonts.load('400 16px Poppins'),
          document.fonts.load('500 16px Poppins'),
          document.fonts.load('600 16px Poppins'),
          document.fonts.load('600 16px Roboto'),
        ])
        
        document.documentElement.classList.remove('fonts-loading')
        document.documentElement.classList.add('fonts-loaded')
      } catch (error) {
        console.warn('Font loading failed:', error)
        // Fallback to system fonts
        document.documentElement.classList.remove('fonts-loading')
        document.documentElement.classList.add('fonts-loaded')
      }
    }
    
    loadFonts()
  }, [])
  
  return null
}
```

---

## 5. Responsive Design Implementation

### Breakpoint Usage

```tsx
// Responsive utility classes for consistent implementation
const responsiveClasses = {
  // Typography scaling
  heroTitle: "text-4xl md:text-6xl lg:text-hero",
  pageTitle: "text-3xl md:text-5xl lg:text-display",
  sectionTitle: "text-2xl md:text-3xl lg:text-heading-1",
  
  // Spacing
  sectionPadding: "py-12 md:py-20 lg:py-32",
  containerPadding: "px-4 sm:px-6 lg:px-8",
  
  // Grid layouts
  featuresGrid: "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8",
  heroLayout: "flex flex-col lg:flex-row items-center gap-8 lg:gap-16",
}
```

---

## 6. Accessibility Implementation

### Focus Management

```tsx
// components/AccessibilityHelpers.tsx
export function SkipLink() {
  return (
    <a
      href="#main"
      className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 z-50 px-4 py-2 bg-fitted-blue text-white rounded-lg focus-fitted"
    >
      Skip to main content
    </a>
  )
}

// Screen reader announcements
export function ScreenReaderAnnouncement({ message }: { message: string }) {
  return (
    <div
      aria-live="polite"
      aria-atomic="true"
      className="sr-only"
    >
      {message}
    </div>
  )
}
```

---

## 7. Implementation Checklist

### Immediate Actions
- [ ] Update `tailwind.config.js` with Fitted Automation colors and fonts
- [ ] Replace existing color variables in CSS/components
- [ ] Update font imports and loading strategy
- [ ] Apply new button and card styling patterns
- [ ] Test responsive behavior at all breakpoints

### Component Updates
- [ ] Update header/navigation with new styling
- [ ] Apply brand colors to hero section
- [ ] Style voice interface with new design system
- [ ] Update feature cards with consistent styling
- [ ] Ensure all interactive states follow guidelines

### Quality Assurance
- [ ] Verify color contrast meets WCAG AA standards
- [ ] Test keyboard navigation functionality
- [ ] Validate responsive design at 375px, 768px, 1440px
- [ ] Check font loading performance
- [ ] Test all interactive states (hover, focus, active)

### Performance Testing
- [ ] Measure page load times with new fonts
- [ ] Optimize font loading strategy
- [ ] Test on slower connections
- [ ] Validate Core Web Vitals scores

---

## 8. Brand Integration Examples

### Loading States

```tsx
export function LoadingSpinner() {
  return (
    <div className="inline-flex items-center justify-center">
      <div className="animate-spin rounded-full h-8 w-8 border-2 border-fitted-blue border-t-transparent"></div>
      <span className="ml-3 text-body text-white/80">Processing...</span>
    </div>
  )
}
```

### Voice Status Indicators

```tsx
export function VoiceStatus({ status }: { status: 'idle' | 'listening' | 'processing' | 'speaking' }) {
  const statusConfig = {
    idle: { color: 'text-white/60', bg: 'bg-fitted-slate', text: 'Ready to listen' },
    listening: { color: 'text-fitted-blue', bg: 'bg-fitted-blue/20', text: 'Listening...' },
    processing: { color: 'text-yellow-400', bg: 'bg-yellow-400/20', text: 'Processing...' },
    speaking: { color: 'text-green-400', bg: 'bg-green-400/20', text: 'Speaking...' },
  }
  
  const config = statusConfig[status]
  
  return (
    <div className={`inline-flex items-center px-3 py-1 rounded-full ${config.bg} ${config.color} text-sm font-medium`}>
      <div className={`w-2 h-2 rounded-full ${config.color.replace('text-', 'bg-')} mr-2 ${status === 'listening' ? 'animate-pulse' : ''}`} />
      {config.text}
    </div>
  )
}
```

This implementation guide provides a complete framework for applying Fitted Automation's brand guidelines to your Voice AI Assistant, ensuring visual consistency, performance optimization, and accessibility compliance.