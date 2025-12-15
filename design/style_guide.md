# Global Excellence Scholarship - Unified Style Guide

**Version:** 1.0  
**Last Updated:** December 2025  
**Purpose:** Ensure consistent design across all pages and components

---

## 1. COLOR PALETTE

### Primary Colors
| Color | Hex Code | Usage | CSS Variable |
|-------|----------|-------|--------------|
| **Primary Navy** | `#003366` | Headers, buttons, accents, CTAs | `--color-primary` |
| **Primary Yellow** | `#f1c40f` | Highlights, accents, secondary CTAs | `--color-accent` |
| **Dark Navy (Hover)** | `#002244` | Button hover states | `--color-primary-hover` |

### Neutral Colors
| Color | Hex Code | Usage | CSS Variable |
|-------|----------|-------|--------------|
| **White** | `#ffffff` | Card backgrounds, text backgrounds | `--color-white` |
| **Light Gray** | `#f4f4f9` | Page background | `--color-bg-light` |
| **Light Blue-Gray** | `#e8ecf1` | Hero sections, info boxes | `--color-bg-secondary` |
| **Medium Gray** | `#555` | Body text | `--color-text-secondary` |
| **Dark Gray** | `#333` | Headings (secondary) | `--color-text-dark` |
| **Border Gray** | `#ccc` | Form borders | `--color-border` |
| **Light Border** | `#eee` | Dividers | `--color-border-light` |
| **Footer Dark** | `#222` | Footer background | `--color-footer-bg` |
| **Footer Text** | `#ddd` | Footer text | `--color-footer-text` |

### Status Colors
| Color | Hex Code | Usage | CSS Variable |
|-------|----------|-------|--------------|
| **Success Green** | `#e6ffed` (bg), `#14532d` (text) | Success messages | `--color-success` |
| **Error Red** | `#fee2e2` (bg), `#7f1d1d` (text), `#c0392b` (closed) | Error messages, closed status | `--color-error` |

### CSS Variables (Add to `<style>` in `base.html`)
```css
:root {
  /* Primary Colors */
  --color-primary: #003366;
  --color-primary-hover: #002244;
  --color-accent: #f1c40f;
  
  /* Neutral Colors */
  --color-white: #ffffff;
  --color-bg-light: #f4f4f9;
  --color-bg-secondary: #e8ecf1;
  --color-text-primary: #003366;
  --color-text-secondary: #555;
  --color-text-dark: #333;
  --color-border: #ccc;
  --color-border-light: #eee;
  --color-footer-bg: #222;
  --color-footer-text: #ddd;
  
  /* Status Colors */
  --color-success-bg: #e6ffed;
  --color-success-text: #14532d;
  --color-error-bg: #fee2e2;
  --color-error-text: #7f1d1d;
  --color-error: #c0392b;
}
```

---

## 2. TYPOGRAPHY

### Font Family
| Element | Font Stack | CSS Variable |
|---------|-----------|--------------|
| **Body & UI** | `'Segoe UI', sans-serif` | `--font-family-base` |

### Font Sizes
| Size | Value | Usage | CSS Variable |
|------|-------|-------|--------------|
| **H1** | `2.5rem` (40px) | Page titles, main hero | `--font-size-h1` |
| **H2** | `1.75rem` (28px) | Section headers | `--font-size-h2` |
| **H3** | `1.25rem` (20px) | Subsection headers | `--font-size-h3` |
| **H4** | `1.1rem` (18px) | Card titles | `--font-size-h4` |
| **Body** | `1rem` (16px) | Default text | `--font-size-body` |
| **Small** | `0.85rem` (14px) | Form labels, metadata | `--font-size-small` |
| **Large** | `1.2rem` (19px) | Hero subtext | `--font-size-large` |

### Font Weights
| Weight | Value | Usage | CSS Variable |
|--------|-------|-------|--------------|
| **Regular** | `400` | Body text | `--font-weight-regular` |
| **Medium** | `600` | Labels, bold text | `--font-weight-medium` |
| **Bold** | `700` | Button text, strong emphasis | `--font-weight-bold` |

### Line Height
| Usage | Value | CSS Variable |
|-------|-------|--------------|
| **Body text** | `1.6` | `--line-height-body` |
| **Headings** | `1.2` | `--line-height-heading` |

### CSS Variables
```css
:root {
  /* Typography */
  --font-family-base: 'Segoe UI', sans-serif;
  --font-size-h1: 2.5rem;
  --font-size-h2: 1.75rem;
  --font-size-h3: 1.25rem;
  --font-size-h4: 1.1rem;
  --font-size-body: 1rem;
  --font-size-small: 0.85rem;
  --font-size-large: 1.2rem;
  --font-weight-regular: 400;
  --font-weight-medium: 600;
  --font-weight-bold: 700;
  --line-height-body: 1.6;
  --line-height-heading: 1.2;
}
```

---

## 3. SPACING SYSTEM

Consistent spacing ensures visual harmony across the site.

### Spacing Scale
| Scale | Value | Usage | CSS Variable |
|-------|-------|-------|--------------|
| **XS** | `0.5rem` (8px) | Small gaps, padding | `--space-xs` |
| **SM** | `1rem` (16px) | Small sections | `--space-sm` |
| **MD** | `1.5rem` (24px) | Medium sections | `--space-md` |
| **LG** | `2rem` (32px) | Large sections | `--space-lg` |
| **XL** | `3rem` (48px) | Major sections | `--space-xl` |

### Margin & Padding Guidelines
- **Hero section padding:** `4rem 5%` (vertical/horizontal)
- **Main container margin:** `2rem auto`
- **Container padding:** `0 2rem`
- **Card padding:** `2rem`
- **Form group margin:** `1.5rem`
- **Footer padding:** `3rem 5%`

### CSS Variables
```css
:root {
  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
}
```

---

## 4. LAYOUT & CONTAINERS

### Max-Width Constraints
| Container | Max-Width | Usage |
|-----------|-----------|-------|
| **Main content** | `1000px` | Sections, forms |
| **Scholarship grid** | `1200px` | Card grids |
| **Navigation** | `1200px` | Header/footer content |
| **Contact/Form** | `600px - 700px` | Single-column layouts |

### Grid System
**Scholarship Cards:**
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 2rem;
```

### Flexbox Patterns
**Navigation:**
```css
display: flex;
justify-content: space-between;
align-items: center;
gap: 30px;
```

---

## 5. UI COMPONENTS

### 5.1 BUTTONS

#### Primary Button (CTA)
```css
background-color: var(--color-primary); /* #003366 */
color: white;
padding: 15px 30px;
text-decoration: none;
border-radius: 5px;
font-weight: bold;
cursor: pointer;
transition: background 0.3s;
```
**Hover State:** `background-color: #002244`

**Usage:** Start Application, Submit Application, Apply Now buttons

---

#### Secondary Button
```css
background-color: var(--color-accent); /* #f1c40f */
color: var(--color-primary); /* #003366 */
padding: 10px 25px;
text-decoration: none;
font-weight: bold;
border-radius: 5px;
```

**Usage:** Login button

---

#### Link Button
```css
color: var(--color-primary);
font-weight: bold;
text-decoration: none;
border-bottom: 2px solid var(--color-accent);
```

**Usage:** "Apply Now →" links on scholarship cards

---

### 5.2 FORMS

#### Form Container
```css
background: white;
max-width: 700px;
margin: 3rem auto;
padding: 2.5rem;
border-radius: 8px;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
```

#### Form Group
```css
margin-bottom: 1.5rem;
```

#### Labels
```css
display: block;
margin-bottom: 0.5rem;
color: var(--color-primary);
font-weight: 600;
font-size: var(--font-size-small);
```

#### Input Fields
```css
width: 100%;
padding: 12px;
border: 1px solid var(--color-border);
border-radius: 4px;
font-size: 1rem;
font-family: inherit;
box-sizing: border-box;
```

**Elements:** `input[type="text"]`, `input[type="email"]`, `input[type="tel"]`, `input[type="date"]`, `input[type="number"]`, `textarea`, `select`

#### Focus State
```css
border-color: var(--color-primary);
outline: none;
box-shadow: 0 0 5px rgba(0, 51, 102, 0.2);
```

#### Two-Column Row
```css
.row {
  display: flex;
  gap: 1rem;
}
.row .form-group {
  flex: 1;
}
```

---

### 5.3 CARDS

#### Card Component
```css
background: white;
border-radius: 8px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
padding: 2rem;
transition: transform 0.2s;
border-top: 5px solid var(--color-primary);
```

**Hover State:**
```css
transform: translateY(-5px);
```

#### Card Header
```css
h3 { 
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}
```

#### Card Amount (Scholarship Cards)
```css
color: var(--color-accent);
font-weight: bold;
font-size: 1.2rem;
margin-bottom: 1rem;
display: block;
```

---

### 5.4 HERO SECTION

#### Hero Container
```css
background-color: var(--color-bg-secondary); /* #e8ecf1 */
padding: 4rem 5%;
text-align: center;
border-bottom: 5px solid var(--color-primary);
```

#### Hero Title
```css
h1 {
  color: var(--color-primary);
  font-size: var(--font-size-h1);
  margin-bottom: 1rem;
}
```

#### Hero Subtitle
```css
p {
  color: var(--color-text-secondary);
  font-size: var(--font-size-large);
  max-width: 700px;
  margin: 0 auto 2rem auto;
}
```

---

### 5.5 SECTIONS

#### Section Container
```css
background: white;
padding: 2rem;
margin-bottom: 3rem;
border-radius: 8px;
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
```

#### Section Header
```css
h2 {
  color: var(--color-primary);
}
```

---

### 5.6 MESSAGES & ALERTS

#### Success Message
```css
padding: 1rem;
margin-bottom: 1rem;
border-radius: 4px;
background: var(--color-success-bg);
color: var(--color-success-text);
border: 1px solid #bbf7d0;
```

#### Error Message
```css
padding: 1rem;
margin-bottom: 1rem;
border-radius: 4px;
background: var(--color-error-bg);
color: var(--color-error-text);
border: 1px solid #fecaca;
```

#### Info Box (Contact Page)
```css
background-color: var(--color-bg-secondary);
padding: 20px;
border-radius: 5px;
font-size: 1rem;
border-left: 5px solid var(--color-primary);
```

---

### 5.7 NAVIGATION

#### Header
```css
background-color: var(--color-primary);
```

#### Navigation Container
```css
display: flex;
justify-content: space-between;
align-items: center;
padding: 1rem 5%;
max-width: 1200px;
margin: 0 auto;
```

#### Nav Links
```css
list-style: none;
display: flex;
gap: 30px;

a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}
```

#### Login Button (in Nav)
```css
background-color: var(--color-accent);
color: var(--color-primary);
padding: 10px 25px;
text-decoration: none;
font-weight: bold;
border-radius: 5px;
```

---

### 5.8 FOOTER

#### Footer Container
```css
background-color: var(--color-footer-bg);
color: var(--color-footer-text);
padding: 3rem 5%;
margin-top: auto;
```

#### Footer Content Layout
```css
display: flex;
justify-content: space-between;
max-width: 1200px;
margin: 0 auto;
```

---

### 5.9 TABLE

#### Table Styling
```css
width: 100%;
max-width: 400px;
font-size: 1rem;
color: var(--color-text-dark);

tr td {
  padding: 5px 0;
}

tr td:last-child {
  text-align: right;
}
```

**Closed Status:** `color: #c0392b`

---

## 6. SHADOWS & BORDERS

### Box Shadows
| Usage | CSS | CSS Variable |
|-------|-----|--------------|
| **Light shadow** | `0 2px 10px rgba(0, 0, 0, 0.05)` | `--shadow-light` |
| **Medium shadow** | `0 2px 8px rgba(0, 0, 0, 0.1)` | `--shadow-medium` |
| **Strong shadow** | `0 4px 15px rgba(0, 0, 0, 0.1)` | `--shadow-strong` |

### Border Radius
| Usage | Value | CSS Variable |
|-------|-------|--------------|
| **Small (inputs, buttons)** | `4px` | `--radius-small` |
| **Medium (cards)** | `8px` | `--radius-medium` |
| **Large** | `5px` | `--radius-button` |

---

## 7. RESPONSIVE DESIGN

### Breakpoints
- **Mobile:** 320px - 480px
- **Tablet:** 481px - 768px
- **Desktop:** 769px and above

### Responsive Guidelines
- **Main container:** Use `padding: 0 2rem` for mobile, adjust with media queries
- **Hero section:** Keep `padding: 4rem 5%` consistent
- **Grid:** Use `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))` for auto-responsive cards
- **Form rows:** Stack on mobile using `flex-direction: column`

### Mobile-First Example
```css
/* Mobile first */
.row {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Tablet and up */
@media (min-width: 768px) {
  .row {
    flex-direction: row;
  }
}
```

---

## 8. IMPLEMENTATION CHECKLIST

### When Creating New Pages:
- [ ] Use CSS variables for all colors
- [ ] Use font sizes from typography scale
- [ ] Use spacing scale (`--space-*` variables)
- [ ] Follow component patterns (cards, buttons, forms)
- [ ] Include hover/focus states for interactive elements
- [ ] Use consistent border radius
- [ ] Apply appropriate shadows
- [ ] Test on mobile devices
- [ ] Maintain max-width constraints
- [ ] Follow naming conventions

### When Updating Existing Components:
- [ ] Ensure color consistency with palette
- [ ] Match spacing to scale
- [ ] Update only styles, not HTML structure
- [ ] Test across pages
- [ ] Check responsive behavior
- [ ] Verify accessibility (color contrast, focus states)

---

## 9. CSS CUSTOM PROPERTIES COMPLETE SET

Add this to `<style>` in `base.html`:

```css
:root {
  /* Primary Colors */
  --color-primary: #003366;
  --color-primary-hover: #002244;
  --color-accent: #f1c40f;
  
  /* Neutral Colors */
  --color-white: #ffffff;
  --color-bg-light: #f4f4f9;
  --color-bg-secondary: #e8ecf1;
  --color-text-primary: #003366;
  --color-text-secondary: #555;
  --color-text-dark: #333;
  --color-border: #ccc;
  --color-border-light: #eee;
  --color-footer-bg: #222;
  --color-footer-text: #ddd;
  
  /* Status Colors */
  --color-success-bg: #e6ffed;
  --color-success-text: #14532d;
  --color-error-bg: #fee2e2;
  --color-error-text: #7f1d1d;
  --color-error: #c0392b;
  
  /* Typography */
  --font-family-base: 'Segoe UI', sans-serif;
  --font-size-h1: 2.5rem;
  --font-size-h2: 1.75rem;
  --font-size-h3: 1.25rem;
  --font-size-h4: 1.1rem;
  --font-size-body: 1rem;
  --font-size-small: 0.85rem;
  --font-size-large: 1.2rem;
  --font-weight-regular: 400;
  --font-weight-medium: 600;
  --font-weight-bold: 700;
  --line-height-body: 1.6;
  --line-height-heading: 1.2;
  
  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
  
  /* Shadows */
  --shadow-light: 0 2px 10px rgba(0, 0, 0, 0.05);
  --shadow-medium: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-strong: 0 4px 15px rgba(0, 0, 0, 0.1);
  
  /* Border Radius */
  --radius-small: 4px;
  --radius-medium: 8px;
  --radius-button: 5px;
}
```

---

## 10. QUICK REFERENCE COLORS

For quick copy-paste reference:

```
Primary Navy: #003366
Dark Navy Hover: #002244
Yellow Accent: #f1c40f
Light Gray Background: #f4f4f9
Light Blue-Gray: #e8ecf1
Success Green Text: #14532d
Success Green BG: #e6ffed
Error Red Text: #7f1d1d
Error Red BG: #fee2e2
Error Red Closed: #c0392b
```

---

## 11. USAGE EXAMPLES

### Example: Creating a New Card
```html
<div class="card" style="
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  padding: 2rem;
  border-top: 5px solid #003366;
">
  <h3 style="color: #003366; margin-bottom: 0.5rem;">Title</h3>
  <p style="color: #555; margin-bottom: 1.5rem;">Description</p>
</div>
```

### Example: Creating a Form Group
```html
<div class="form-group" style="margin-bottom: 1.5rem;">
  <label style="
    display: block;
    margin-bottom: 0.5rem;
    color: #003366;
    font-weight: 600;
  ">Label</label>
  <input type="text" style="
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
  ">
</div>
```

### Example: Creating a Button
```html
<a href="#" style="
  background-color: #003366;
  color: white;
  padding: 15px 30px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
  display: inline-block;
  transition: background 0.3s;
" onmouseover="this.style.backgroundColor='#002244'" 
  onmouseout="this.style.backgroundColor='#003366'">
  Button Text
</a>
```

---

## 12. NOTES FOR DEVELOPERS

1. **Consistency First:** Always reference this guide before styling new components
2. **CSS Variables:** Use `var(--color-*)`, `var(--space-*)`, etc., to maintain consistency
3. **Mobile Responsive:** Test all components on mobile (320px) and tablet (768px) views
4. **Accessibility:** Ensure color contrast ratios meet WCAG standards (4.5:1 for normal text)
5. **Hover States:** All interactive elements should have clear hover/focus states
6. **Shadows:** Use shadows to create depth and hierarchy
7. **Typography:** Maintain font hierarchy—don't mix font families
8. **Spacing:** Use the spacing scale; avoid arbitrary margins/padding
9. **Max-Widths:** Keep content readable by constraining max-widths (1000-1200px)
10. **Testing:** Test across Chrome, Firefox, Safari, and Edge browsers

---

**End of Style Guide**
