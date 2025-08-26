# Fitted Automation Brand Guidelines

## Brand Overview

**Company**: Fitted Automation  
**Industry**: AI Solutions & Automation Technology  
**Brand Positioning**: Professional, cutting-edge AI solutions provider targeting tech-savvy businesses  
**Brand Personality**: Modern, Technical, Performance-focused, User-centric  

---

## Color Palette

### Primary Colors

| Color Name | Hex Code | RGB Values | Usage |
|------------|----------|------------|--------|
| **Navy Blue** | `#0B213E` | RGB(11, 33, 62) | Primary background, brand foundation |
| **Bright Blue** | `#0074FF` | RGB(0, 116, 255) | Primary accent, CTAs, interactive elements |
| **White** | `#FFFFFF` | RGB(255, 255, 255) | Primary text on dark backgrounds |
| **Dark Gray** | `#313131` | RGB(49, 49, 49) | Secondary text, content hierarchy |
| **Slate Background** | `#0F172A` | RGB(15, 23, 42) | Secondary background, sections |

### Color Usage Guidelines

- **Navy Blue (#0B213E)**: Use as primary background color for hero sections and main page backgrounds
- **Bright Blue (#0074FF)**: Reserve for interactive elements, CTAs, links, and brand accents
- **White (#FFFFFF)**: Primary text color on dark backgrounds, ensures high contrast and readability
- **Dark Gray (#313131)**: Use for secondary text, descriptions, and content that needs hierarchy
- **Slate Background (#0F172A)**: Alternative background for creating visual depth and section separation

### Accessibility Standards
- All color combinations meet WCAG 2.1 AA contrast requirements
- Navy Blue + White: 14.6:1 contrast ratio (AAA level)
- Bright Blue + White: 3.1:1 contrast ratio (AA level for large text)

---

## Typography

### Font Families

#### Primary Font Stack
```css
font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

#### Secondary Font Stack
```css
font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Font Weights
- **Poppins**: 400 (Regular), 500 (Medium), 600 (Semi-Bold)
- **Roboto**: 600 (Semi-Bold)

### Typography Scale

| Element | Font Family | Size | Weight | Line Height | Usage |
|---------|-------------|------|--------|-------------|--------|
| **Hero Title** | Poppins | 180px / 11.25rem | 600 | 1.1 | Landing page headlines |
| **H1** | Poppins | 64px / 4rem | 600 | 1.2 | Page titles |
| **H2** | Poppins | 45px / 2.8rem | 600 | 1.3 | Section headers |
| **H3** | Poppins | 36px / 2.25rem | 500 | 1.4 | Subsection titles |
| **H4** | Poppins | 32px / 2rem | 500 | 1.4 | Component headers |
| **H5** | Poppins | 30px / 1.875rem | 500 | 1.5 | Card titles |
| **Body Large** | Poppins | 27px / 1.6875rem | 400 | 1.6 | Lead text |
| **Body Regular** | Poppins | 24px / 1.5rem | 400 | 1.6 | Standard body text |
| **Body Small** | Roboto | 26px / 1.625rem | 600 | 1.5 | UI elements |

### Responsive Typography
- Mobile-first approach with breakpoint at 768px
- Text sizes scale down appropriately for mobile devices
- Maintain readability across all viewport sizes

---

## Layout & Spacing

### Grid System
- **Flexbox-based layout** with utility-first approach
- **Mobile-first responsive design** (768px breakpoint)
- **Container widths**: Fluid with max-width constraints
- **Aspect ratios**: 16:9 for hero images and media

### Spacing Scale (Tailwind-based)

| Class | Value | Pixels | Usage |
|-------|-------|--------|--------|
| `gap-2` | 0.5rem | 8px | Tight element spacing |
| `gap-4` | 1rem | 16px | Standard component gaps |
| `gap-6` | 1.5rem | 24px | Section spacing |
| `gap-8` | 2rem | 32px | Large component separation |
| `gap-12` | 3rem | 48px | Major section breaks |

### Padding & Margins
- **Micro spacing**: 2-4 (8px-16px) for buttons, form elements
- **Component spacing**: 4-6 (16px-24px) for cards, content blocks  
- **Section spacing**: 8-12 (32px-48px) for major layout divisions
- **Page margins**: 16-24 (64px-96px) for container boundaries

---

## Interactive Elements

### Button Styling
```css
/* Primary Button */
.btn-primary {
  background-color: #0074FF;
  color: #FFFFFF;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056CC;
  transform: translateY(-1px);
}
```

### Link Styling
```css
.link-primary {
  color: #0074FF;
  text-decoration: none;
  transition: color 0.2s ease;
}

.link-primary:hover {
  color: #FFFFFF;
}
```

### Interactive States
- **Hover**: Subtle color transitions (0.2-0.3s ease)
- **Focus**: Visible focus rings for accessibility
- **Active**: Slight transform effects (translateY)

---

## Performance Optimization

### Font Loading Strategy
```javascript
// Font loading optimization with fallbacks
font-display: swap;
// Preload critical fonts
<link rel="preload" href="fonts/poppins.woff2" as="font" type="font/woff2" crossorigin>
```

### Image Optimization
- **Aspect ratio control**: 16:9 for hero images
- **Responsive loading**: Conditional preloading based on viewport
- **Lazy loading**: For non-critical images

---

## Brand Voice & Messaging

### Brand Characteristics
- **Professional**: Authoritative and credible in AI/automation space
- **Technical**: Demonstrates deep technical expertise
- **Performance-focused**: Emphasizes efficiency and optimization
- **User-centric**: Prioritizes user experience and accessibility

### Messaging Themes
- AI-powered automation solutions
- Cutting-edge technology
- Performance and reliability
- Professional expertise
- User experience excellence

---

## Component Patterns

### Card Components
- **Background**: Slate (#0F172A) or Navy (#0B213E)
- **Borders**: Subtle or none
- **Padding**: 24px-32px (gap-6 to gap-8)
- **Typography**: Poppins for headings, mixed for content

### Navigation
- **Background**: Navy Blue (#0B213E)
- **Links**: White text with blue hover states
- **Mobile**: Collapsible menu pattern
- **Spacing**: Consistent gap utilities

### Forms
- **Input fields**: Dark backgrounds with light text
- **Labels**: Clear hierarchy with proper associations
- **Buttons**: Primary blue for actions
- **Validation**: Clear error states and feedback

---

## Accessibility Guidelines

### WCAG 2.1 AA Compliance
- **Color contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Focus indicators**: Visible focus states on all interactive elements
- **Keyboard navigation**: Full keyboard accessibility
- **Screen readers**: Proper semantic HTML and ARIA labels

### Implementation Checklist
- [ ] Alt text for all images
- [ ] Proper heading hierarchy (H1-H6)
- [ ] Form labels properly associated
- [ ] Focus management for interactive elements
- [ ] Color is not the only means of conveying information

---

## Technical Implementation Notes

### CSS Variables
```css
:root {
  --background-color: #0B213E;
  --primary-color: #0074FF;
  --text-primary: #FFFFFF;
  --text-secondary: #313131;
  --background-alt: #0F172A;
}
```

### Tailwind Configuration
```javascript
// Custom colors for Tailwind
theme: {
  colors: {
    'navy': '#0B213E',
    'blue-primary': '#0074FF',
    'slate-dark': '#0F172A',
    'gray-text': '#313131'
  }
}
```

---

## Quality Assurance

### Design Review Checklist
- [ ] Color palette consistency across all components
- [ ] Typography hierarchy properly implemented
- [ ] Responsive behavior at all breakpoints
- [ ] Interactive states properly defined
- [ ] Accessibility requirements met
- [ ] Performance optimization applied
- [ ] Brand voice reflected in content

### Testing Requirements
- **Cross-browser compatibility**: Chrome, Firefox, Safari, Edge
- **Device testing**: Desktop (1440px), Tablet (768px), Mobile (375px)
- **Performance**: Page load times under 3 seconds
- **Accessibility**: WCAG 2.1 AA compliance verification