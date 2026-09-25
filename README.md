# Zentro-Moto-Website
Zentro Moto Ecommerce Website

## HIVIS Marketing Roadmap

A static, single-page dashboard (`index.html`, `styles.css`, `script.js`) showing marketing projects across the year, one swimlane per team member.

### Monthly update

Edit the data blocks at the top of `script.js` only:

- `SITE_CONFIG` – "Updated" label, highlighted month (`currentMonth`, 1–12), year.
- `TEAM` – marketing team swimlanes, in display order (these are counted as team members).
- `TEAM_COLOURS` – lane/bar colour per team member (`"blue"`, `"purple"`, `"green"`, `"grey"`).
- `PROJECTS` – one entry per unique project: `id`, `name`, `owners` (e.g. `["Ben", "Steve"]`, or `["Unassigned"]`), `startMonth` / `endMonth` (1–12), `category`, `status` (`"In Progress"`, `"Planned"`, `"Complete"`), `description`.
- `PENDING_PROJECTS` – projects waiting on an owner or dates; not shown until moved into `PROJECTS`.

A shared project is entered once and appears in each owner's lane; the "Active Projects" figure counts unique In Progress projects. Bars span their months automatically and are ordered long-running → current → upcoming. `Unassigned` projects appear in a "Shared / Unassigned" lane at the bottom, which is hidden when empty. Invalid entries are skipped with a warning in the browser console.

### Deploy

No build step. On Netlify, publish the repository root (build command empty, publish directory `.`), or drag the three files into Netlify Drop.
