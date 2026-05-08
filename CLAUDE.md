# countdowns-live — Contexto del proyecto

## Qué es esto
Sitio web dedicado exclusivamente a cuentas regresivas (countdowns) para eventos globales.
Dominio en inglés, apuntado a tráfico internacional.

## Origen
Este proyecto se desprendió de calculadora.live, donde había una sección /countdowns/.
En `countdowns-src/` están los archivos originales de esa sección (engine, CSS, páginas individuales, admin).
Sirven de referencia de lógica y datos, pero el nuevo sitio debe tener diseño e identidad propios.

## Stack
- HTML/CSS/JS puro, sin frameworks ni bundlers
- Archivos estáticos servidos desde GitHub Pages (o Cloudflare Pages / Netlify)
- `countdowns-data.json` → fuente de datos para eventos con fecha variable (se puede editar vía admin o directo en repo)

## Idioma
- **Inglés por defecto**
- Con selector de idioma (EN / ES mínimo) para más adelante
- Los slugs de URL deben ser en inglés desde el inicio: `/countdown/gta6/`, `/countdown/christmas/`, etc.

## Estructura objetivo
```
/                        ← Hub con todos los countdowns agrupados por categoría
/countdown/[slug]/       ← Página individual por evento (con timer en vivo, artículo, FAQ)
/admin/                  ← Panel de admin con GitHub API para actualizar fechas
countdowns-data.json     ← Datos de eventos con fecha variable
```

## Categorías de eventos (referencia, pueden cambiar)
- Releases (GTA VI, iPhone, consolas, etc.)
- Sports (F1, Champions League, NBA Finals, World Cup 2026, etc.)
- Holidays (Christmas, New Year, Halloween, Valentine's Day, etc.)
- Sales (Black Friday, Cyber Monday, etc.)
- Entertainment (Oscars, Grammys, Met Gala, Coachella, etc.)

## Lógica del engine (referencia — está en countdowns-src/)
- Tres tipos de evento: `auto` (fecha calculada en JS), `variable` (fecha en JSON), `one-time` (muestra "ya ocurrió")
- `CountdownEngine.render(rootId, config)` → construye la página del countdown
- `CountdownEngine.getCardData(config, cb)` → devuelve días restantes para el hub
- Fechas auto incluidas: weekends, next year, holidays, full moons, political dates

## Diseño
- **Identidad visual propia**, distinta a calculadora.live
- Orientada a eventos y tiempo: puede ser más oscura, más dinámica, más visual
- Prioridad: hero con timer grande, categorías claras, carga rápida, SEO fuerte
- Mobile-first

## SEO
- Cada página de countdown necesita: título optimizado, meta description, H1, artículo descriptivo, FAQ con H2/H3
- El hub necesita: descripción general, links internos, estructura semántica
- URLs limpias y en inglés

## Admin
- Panel protegido por contraseña para actualizar fechas en countdowns-data.json vía GitHub API
- Patrón ya probado en calculadora.live (ver countdowns-src/admin/)

## Estado actual
- Archivos de referencia copiados en countdowns-src/
- Repo inicializado, sin deploy configurado aún
- Siguiente paso: diseñar desde cero la identidad y la estructura del sitio
