# Zentro-Moto-Website
Zentro Moto Ecommerce Website

## HIVIS Marketing Roadmap

A static, single-page dashboard (`index.html`, `styles.css`, `script.js`) showing marketing projects across the year, one swimlane per team member.

### Monthly update

Edit the top of `script.js` only:

- `SITE_CONFIG` – "Updated" label, highlighted month (`currentMonth`), summary row values.
- `TEAM` – swimlanes, in display order.
- `PROJECTS` – one entry per bar: `name`, `owner` (a `TEAM` id), `startMonth` / `endMonth` (`"JAN"`–`"DEC"`), `category`, `status` (`"In Progress"`, `"Planned"`, `"Complete"`), `description`.

Overlapping projects in a lane stack automatically. A lane with no projects shows "No current roadmap projects added". Invalid entries are skipped with a warning in the browser console.

### Deploy

No build step. On Netlify, publish the repository root (build command empty, publish directory `.`), or drag the three files into Netlify Drop.
