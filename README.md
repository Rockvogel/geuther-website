# Geuther Website Styleguide

## Inhaltsverzeichnis
- [Grundlegende Setup](#grundlegendes-setup)
- [Farbsystem](#farbsystem)
- [Typografie](#typografie)
- [CSS-Klassennamen](#css-klassennamen)
- [Layout-System](#layout-system)
- [Komponenten](#komponenten)
- [Best Practices](#best-practices)

## Grundlegendes Setup

### Erforderliche Einbindungen
```html
<!-- Schriftart -->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Basis-Styles -->
<link rel="stylesheet" href="all.css">

<!-- Icons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">

<!-- Bootstrap JS (falls benötigt) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

### Basis HTML-Struktur
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seitentitel | Geuther</title>
    <!-- Einbindungen hier -->
</head>
<body>
    <div class="geuther-[seitenname]">
        <div class="container">
            <!-- Inhalt hier -->
        </div>
    </div>
</body>
</html>
```

## Farbsystem

### Hauptfarben
```css
:root {
    --geuther-primary: #42584A;    /* Hauptfarbe, für wichtige Elemente */
    --geuther-secondary: #D4C4B7;  /* Beige Akzentfarbe */
    --geuther-text: #333333;       /* Textfarbe */
    --geuther-bg: #FFFFFF;         /* Hintergrundfarbe */
    --geuther-accent: #F5F1ED;     /* Heller Beige Hintergrund */
    --geuther-border: #E5E5E5;     /* Rahmenfarbe */
}
```

### Farbanwendung
- Primärfarbe: Hauptüberschriften, CTA-Buttons, wichtige UI-Elemente
- Sekundärfarbe: Icons, Hover-Zustände, Badges
- Akzentfarbe: Sektionshintergründe, subtile Hervorhebungen
- Rahmenfarbe: Karten, Trennlinien, subtile Borders

## Typografie

### Schriftfamilie
- Hauptschrift: 'Montserrat', sans-serif

### Schriftgrößen
- Hauptüberschriften: 2.5rem
- Sektionsüberschriften: 2rem
- Kartenüberschriften: 1.2rem
- Normaler Text: 0.95rem - 1.1rem
- Kleine Texte (Badges): 0.9rem

### Schriftgewichte
- Normal: 400
- Medium: 500
- Semibold: 600
- Bold: 700

## CSS-Klassennamen

### Namenskonvention
- Prefix: `geuther-[seitenname]`
- BEM-ähnliche Struktur: `[block]__[element]--[modifier]`

### Beispiele
```css
.geuther-affiliate .hero-section {}
.geuther-affiliate .benefit-card {}
.geuther-affiliate .feature-item {}
```

## Layout-System

### Container
- Maximale Breite: 1200px
- Zentriert mit Auto-Margins
- Padding in mobiler Ansicht: 1rem

### Grid-System
- Desktop: 3 Spalten
- Tablet: 2 Spalten
- Mobil: 1 Spalte

### Abstände
- Sektionen: 4rem (Desktop), 2rem (Mobil)
- Kartenelemente: 2rem Padding
- Grid-Gap: 2rem

## Komponenten

### Karten
```css
.component-card {
    background: var(--geuther-bg);
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid var(--geuther-border);
    transition: all 0.3s ease;
}
```

### Buttons
```css
.cta-button {
    background-color: var(--geuther-primary);
    color: white;
    padding: 1rem 2.5rem;
    border-radius: 8px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}
```

### Badges
```css
.badge {
    background-color: var(--geuther-accent);
    padding: 0.5rem 1.5rem;
    border-radius: 50px;
    font-weight: 500;
    border: 1px solid var(--geuther-secondary);
}
```

### Bilder
```css
.content-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px-12px;
    object-fit: cover;
}
```

## Best Practices

### Responsive Design
- Mobile-First Ansatz
- Breakpoints:
  - Tablet: 992px
  - Mobil: 768px

### Performance
- Bilder mit `loading="lazy"`
- WebP-Format für Bilder
- Optimierte Bildgrößen verwenden

### Accessibility
- Semantisches HTML
- Alt-Texte für Bilder
- ARIA-Labels wo nötig
- Ausreichende Kontrastwerte

### Animation
- Sanfte Übergänge: `transition: all 0.3s ease`
- Hover-Effekte für interaktive Elemente
- Dezente Transformationen (translateY, scale)

### Code-Organisation
- Gruppierung von CSS-Eigenschaften
- Kommentare für komplexe Selektoren
- Wiederverwendbare Klassen für häufige Styles 