/* ==========================================================================
   HIVIS Marketing Roadmap
   ==========================================================================

   MONTHLY UPDATE GUIDE
   --------------------
   You should only ever need to edit the two blocks directly below:

   1. SITE_CONFIG  – "Updated" label, current month highlight, summary stats.
   2. TEAM         – the swimlanes, in display order.
   3. PROJECTS     – one entry per project bar.

   Project fields:
     name         Project name shown on the bar.
     owner        Must match a TEAM id (e.g. "jordan"). A project shared by two
                  people is added once per person so it appears in both lanes.
     startMonth   "JAN" … "DEC"
     endMonth     "JAN" … "DEC" (same as startMonth for a one-month project)
     category     Short label, e.g. "CAMPAIGN", "STRATEGY", "INTERNAL".
     status       "In Progress" | "Planned" | "Complete"
     description  One or two sentences. Shown in the details popover only.

   Keep projects at project level – individual tasks do not belong here.
   ========================================================================== */

const SITE_CONFIG = {
  year: 2026,
  updatedLabel: "Updated September 2026",
  currentMonth: "SEP", // Highlighted column. Set to null to use today's month.

  // Summary row under the header. Edit freely.
  summary: [
    { value: "5", label: "Current Projects" },
    { value: "3", label: "Marketing Team Members" },
    { value: "Updated", label: "Monthly" },
  ],
};

const TEAM = [
  { id: "jordan", name: "Jordan" },
  { id: "ben", name: "Ben" },
  { id: "steve", name: "Steve" },
];

const PROJECTS = [
  // ---- Jordan ------------------------------------------------------------
  {
    name: "Marketing Dashboard",
    owner: "jordan",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "INTERNAL",
    status: "In Progress",
    description:
      "Create a simple annual marketing calendar/dashboard visible to Sales and Management.",
  },
  {
    name: "Industry EDM Campaigns",
    owner: "jordan",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "CAMPAIGN",
    status: "In Progress",
    description:
      "Develop industry-specific EDM campaigns based around key HIVIS product groups.",
  },
  {
    name: "Product Marketing Framework",
    owner: "jordan",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "STRATEGY",
    status: "In Progress",
    description:
      "Define how HIVIS products should be marketed, including messaging, benefits and product positioning.",
  },
  {
    name: "HIVIS Direct Training",
    owner: "jordan",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "SALES SUPPORT",
    status: "In Progress",
    description:
      "Create training material to help Customer Service walk customers through HIVIS Direct from login through to quoting and ordering.",
  },

  // ---- Ben ---------------------------------------------------------------
  // No current roadmap projects. Add entries with owner: "ben" to fill the lane.

  // ---- Steve -------------------------------------------------------------
  {
    name: "Catalogue Update & Reprint",
    owner: "steve",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "CONTENT",
    status: "In Progress",
    description:
      "Review catalogue content, update pricing and prepare the next catalogue run.",
  },
  {
    name: "EDM Campaign Process",
    owner: "steve",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "PROCESS",
    status: "In Progress",
    description:
      "Create a visual process covering an EDM campaign from initial concept through to measurement and debrief.",
  },
  {
    name: "Industry EDM Campaigns",
    owner: "steve",
    startMonth: "SEP",
    endMonth: "OCT",
    category: "CAMPAIGN",
    status: "In Progress",
    description:
      "Work with Jordan on industry-specific EDM campaigns and product content.",
  },
];

/* ==========================================================================
   Rendering – no edits needed below this line for monthly updates.
   ========================================================================== */

const MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];
const MONTH_NAMES = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

const STATUS_CLASS = {
  "In Progress": "in-progress",
  Planned: "planned",
  Complete: "complete",
};

/** Returns a 0-based month index, or -1 if the value is not recognised. */
function monthIndex(value) {
  return MONTHS.indexOf(String(value || "").trim().slice(0, 3).toUpperCase());
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function formatTiming(project) {
  const start = MONTH_NAMES[project.start];
  const end = MONTH_NAMES[project.end];
  return project.start === project.end ? start : `${start} – ${end}`;
}

/** Validates raw project data, warning in the console about anything skipped. */
function normaliseProjects(projects) {
  const teamIds = new Set(TEAM.map((m) => m.id));

  return projects.reduce((valid, raw, i) => {
    const start = monthIndex(raw.startMonth);
    const end = monthIndex(raw.endMonth);
    const problems = [];

    if (!teamIds.has(raw.owner)) problems.push(`unknown owner "${raw.owner}"`);
    if (start < 0) problems.push(`invalid startMonth "${raw.startMonth}"`);
    if (end < 0) problems.push(`invalid endMonth "${raw.endMonth}"`);
    if (start > end) problems.push("startMonth is after endMonth");
    if (!STATUS_CLASS[raw.status]) problems.push(`unknown status "${raw.status}"`);

    if (problems.length) {
      console.warn(`Roadmap: skipped project #${i + 1} "${raw.name}" – ${problems.join(", ")}`);
    } else {
      valid.push({ ...raw, start, end, id: `project-${i}` });
    }
    return valid;
  }, []);
}

/**
 * Packs projects into rows so overlapping bars stack instead of colliding.
 * Returns an array of rows, each an array of projects.
 */
function packRows(projects) {
  const sorted = [...projects].sort((a, b) => a.start - b.start || a.end - b.end);
  const rows = [];

  sorted.forEach((project) => {
    const row = rows.find((r) => r[r.length - 1].end < project.start);
    if (row) row.push(project);
    else rows.push([project]);
  });

  return rows;
}

function getCurrentMonth() {
  const configured = monthIndex(SITE_CONFIG.currentMonth);
  return configured >= 0 ? configured : new Date().getMonth();
}

/* ---------- Header + summary ---------- */

function renderHeader() {
  document.getElementById("updated-label").textContent = SITE_CONFIG.updatedLabel;
  document.getElementById("roadmap-year").textContent = SITE_CONFIG.year;

  const summary = document.getElementById("summary");
  SITE_CONFIG.summary.forEach((item) => {
    const node = el("div", "summary-item");
    node.append(el("strong", "", item.value), el("span", "", item.label));
    summary.append(node);
  });
}

/* ---------- Roadmap ---------- */

function renderMonthHeader(currentMonth) {
  const row = el("div", "roadmap-row roadmap-head");
  row.setAttribute("role", "row");

  const corner = el("div", "roadmap-corner", "Team");
  corner.setAttribute("role", "columnheader");
  row.append(corner);

  MONTHS.forEach((month, i) => {
    const cell = el("div", "month", month);
    cell.setAttribute("role", "columnheader");
    cell.setAttribute("aria-label", MONTH_NAMES[i]);
    if (i < currentMonth) cell.classList.add("is-past");
    if (i === currentMonth) {
      cell.classList.add("is-current");
      cell.setAttribute("aria-current", "date");
      cell.append(el("span", "month-now-tag", "NOW"));
    }
    row.append(cell);
  });

  return row;
}

function renderBar(project, rowIndex) {
  const bar = el("button", `bar bar--${STATUS_CLASS[project.status]}`);
  bar.type = "button";
  bar.dataset.projectId = project.id;
  bar.style.gridColumn = `${project.start + 1} / ${project.end + 2}`;
  bar.style.gridRow = String(rowIndex + 1);
  bar.setAttribute("aria-label", `${project.name}, ${project.category}, ${project.status}, ${formatTiming(project)}`);

  const dot = el("span", `status-dot status-dot--${STATUS_CLASS[project.status]}`);
  dot.title = project.status;

  bar.append(el("span", "bar-name", project.name), el("span", "bar-category", project.category), dot);
  return bar;
}

function renderLane(member, projects, currentMonth) {
  const lane = el("div", "roadmap-row lane");
  lane.setAttribute("role", "row");

  // Sticky name column
  const label = el("div", "lane-label");
  label.setAttribute("role", "rowheader");
  label.append(el("span", "lane-name", member.name));
  const count = projects.length;
  label.append(el("span", "lane-count", count ? `${count} project${count === 1 ? "" : "s"}` : "No active projects"));
  lane.append(label);

  // Track
  const track = el("div", "lane-track");
  track.setAttribute("role", "cell");
  const rows = packRows(projects);
  track.style.gridTemplateRows = `repeat(${Math.max(rows.length, 1)}, auto)`;

  MONTHS.forEach((_, i) => {
    const col = el("div", "track-col");
    col.style.gridColumn = String(i + 1);
    if (i === currentMonth) col.classList.add("is-current");
    col.setAttribute("aria-hidden", "true");
    track.append(col);
  });

  if (count === 0) {
    const empty = el("div", "lane-empty");
    empty.append(el("span", "lane-empty-text", "No current roadmap projects added"));
    empty.style.gridRow = "1";
    track.append(empty);
  } else {
    rows.forEach((row, r) => row.forEach((project) => track.append(renderBar(project, r))));
  }

  lane.append(track);
  return lane;
}

function renderRoadmap(projects) {
  const roadmap = document.getElementById("roadmap");
  const currentMonth = getCurrentMonth();

  roadmap.append(renderMonthHeader(currentMonth));
  TEAM.forEach((member) => {
    const own = projects.filter((p) => p.owner === member.id);
    roadmap.append(renderLane(member, own, currentMonth));
  });

  scrollCurrentMonthIntoView(currentMonth);
}

/** On narrow screens, start the horizontal scroll near the current month. */
function scrollCurrentMonthIntoView(currentMonth) {
  const scroller = document.getElementById("roadmap-scroll");
  if (scroller.scrollWidth <= scroller.clientWidth) return;

  const monthCell = scroller.querySelectorAll(".month")[currentMonth];
  const labelWidth = scroller.querySelector(".roadmap-corner").offsetWidth;
  scroller.scrollLeft = Math.max(0, monthCell.offsetLeft - labelWidth - monthCell.offsetWidth * 2);
}

/* ---------- Popover ---------- */

function setupPopover(projects) {
  const byId = new Map(projects.map((p) => [p.id, p]));
  const teamName = new Map(TEAM.map((m) => [m.id, m.name]));
  const popover = document.getElementById("popover");
  const roadmap = document.getElementById("roadmap");
  const scroller = document.getElementById("roadmap-scroll");

  let activeBar = null;
  let pinned = false;
  let suppressFocusPreview = false; // avoids re-opening when focus returns after closing

  function fill(project) {
    document.getElementById("popover-category").textContent = project.category;
    document.getElementById("popover-title").textContent = project.name;
    document.getElementById("popover-owner").textContent = teamName.get(project.owner);
    document.getElementById("popover-timing").textContent = formatTiming(project);
    document.getElementById("popover-description").textContent = project.description;

    const status = document.getElementById("popover-status");
    status.replaceChildren(
      el("span", `status-dot status-dot--${STATUS_CLASS[project.status]}`),
      document.createTextNode(project.status)
    );
  }

  function position() {
    if (!activeBar) return;
    const gap = 8;
    const margin = 12;
    const rect = activeBar.getBoundingClientRect();
    const pop = popover.getBoundingClientRect();

    let top = rect.bottom + gap;
    if (top + pop.height > window.innerHeight - margin && rect.top - gap - pop.height > margin) {
      top = rect.top - gap - pop.height; // flip above
    }
    const left = Math.min(Math.max(rect.left, margin), window.innerWidth - pop.width - margin);

    popover.style.top = `${Math.round(top)}px`;
    popover.style.left = `${Math.round(left)}px`;
  }

  function show(bar, pin) {
    const project = byId.get(bar.dataset.projectId);
    if (!project) return;

    if (activeBar && activeBar !== bar) activeBar.classList.remove("is-active");
    activeBar = bar;
    pinned = pin;
    bar.classList.add("is-active");
    bar.setAttribute("aria-expanded", "true");
    popover.classList.toggle("is-pinned", pin);

    fill(project);
    popover.hidden = false;
    position();
  }

  function hide() {
    if (activeBar) {
      activeBar.classList.remove("is-active");
      activeBar.setAttribute("aria-expanded", "false");
    }
    activeBar = null;
    pinned = false;
    popover.hidden = true;
  }

  // Hover preview
  roadmap.addEventListener("mouseover", (e) => {
    const bar = e.target.closest(".bar");
    if (bar && !pinned && bar !== activeBar) show(bar, false);
  });
  roadmap.addEventListener("mouseout", (e) => {
    const bar = e.target.closest(".bar");
    if (bar && !pinned && !bar.contains(e.relatedTarget)) hide();
  });

  // Click pins the popover open (also covers touch devices)
  roadmap.addEventListener("click", (e) => {
    const bar = e.target.closest(".bar");
    if (!bar) return;
    if (pinned && bar === activeBar) hide();
    else show(bar, true);
  });

  // Keyboard focus shows a preview
  roadmap.addEventListener("focusin", (e) => {
    const bar = e.target.closest(".bar");
    if (bar && !pinned && !suppressFocusPreview) show(bar, false);
  });
  roadmap.addEventListener("focusout", (e) => {
    if (!pinned && e.target.closest(".bar")) hide();
  });

  function closeAndRefocus() {
    const bar = activeBar;
    hide();
    if (!bar) return;
    suppressFocusPreview = true;
    bar.focus();
    suppressFocusPreview = false;
  }

  document.getElementById("popover-close").addEventListener("click", closeAndRefocus);

  document.addEventListener("click", (e) => {
    if (pinned && !popover.contains(e.target) && !e.target.closest(".bar")) hide();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && activeBar) closeAndRefocus();
  });

  window.addEventListener("resize", position);
  window.addEventListener("scroll", position, { passive: true });
  scroller.addEventListener("scroll", position, { passive: true });
}

/* ---------- Init ---------- */

document.addEventListener("DOMContentLoaded", () => {
  const projects = normaliseProjects(PROJECTS);
  renderHeader();
  renderRoadmap(projects);
  setupPopover(projects);
});
