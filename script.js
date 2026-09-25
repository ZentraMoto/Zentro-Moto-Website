/* ==========================================================================
   HIVIS Marketing Roadmap
   ==========================================================================

   MONTHLY UPDATE GUIDE
   --------------------
   You should only ever need to edit the data blocks directly below:

   1. SITE_CONFIG       – "Updated" label, highlighted month, year.
   2. TEAM              – the marketing team swimlanes, in display order.
   3. PROJECTS          – one entry per unique project.
   4. PENDING_PROJECTS  – projects waiting on an owner or dates (not shown).

   Project fields:
     id           Unique, lowercase, no spaces (e.g. "website-epicor").
     name         Project name shown on the bar.
     owners       Array of TEAM names, e.g. ["Jordan"] or ["Ben", "Steve"].
                  A shared project is entered ONCE and appears in every
                  owner's lane, but is only counted once in the summary.
                  Use ["Unassigned"] until an owner is confirmed.
     startMonth   1–12 (1 = January). "SEP" style names also work.
     endMonth     1–12, same as startMonth for a one-month project.
     category     Short label, e.g. "CAMPAIGN", "STRATEGY", "WEBSITE".
     status       "In Progress" | "Planned" | "Complete"
     description  One or two sentences. Shown in the details popover only.

   Bars are ordered automatically within each lane: long-running projects
   first, then current, then upcoming.

   Keep projects at project level – individual tasks do not belong here.
   ========================================================================== */

const SITE_CONFIG = {
  year: 2026,
  updatedLabel: "Updated September 2026",
  currentMonth: 9, // Highlighted "NOW" column (1–12). Set to null to use today's month.
  updateFrequency: "Monthly", // Shown in the summary row as "Updated Monthly".
};

// Marketing team swimlanes, in display order. Only these count as team members.
const TEAM = ["Jordan", "Ben", "Steve"];

// Projects with owners: ["Unassigned"] appear in this understated lane at the bottom.
const UNASSIGNED = "Unassigned";
const UNASSIGNED_LANE_LABEL = "Shared / Unassigned";

const PROJECTS = [
  // ---- Ongoing (full year) ----------------------------------------------
  {
    id: "website-product-content",
    name: "Website Product Content Updates",
    owners: ["Jordan"],
    startMonth: 1,
    endMonth: 12,
    category: "WEBSITE",
    status: "In Progress",
    description:
      "Ongoing improvement of product information, content and marketing messaging across the HIVIS website.",
  },
  {
    id: "ultimate-vehicle-wraps-content",
    name: "Ultimate Vehicle Wraps – Imagery & Posts",
    owners: ["Jordan"],
    startMonth: 1,
    endMonth: 12,
    category: "CONTENT",
    status: "In Progress",
    description:
      "Ongoing creation and management of imagery, social media posts and marketing content for Ultimate Vehicle Wraps throughout the year.",
  },
  {
    id: "google-ads",
    name: "Google Ads Campaign",
    owners: ["Steve"],
    startMonth: 1,
    endMonth: 12,
    category: "DIGITAL",
    status: "In Progress",
    description: "Ongoing Google Ads campaign management and optimisation throughout the year.",
  },

  // ---- Started earlier in the year --------------------------------------
  {
    id: "hivis-tech",
    name: "HIVIS Tech",
    owners: ["Jordan"],
    startMonth: 7,
    endMonth: 11,
    category: "PRODUCT / STRATEGY",
    status: "In Progress",
    description: "Marketing and development activity relating to the HIVIS Tech offering.",
  },
  {
    id: "website-epicor",
    name: "Website Epicor Integration",
    owners: ["Ben", "Steve"],
    startMonth: 7,
    endMonth: 9,
    category: "WEBSITE",
    status: "In Progress",
    description: "Integration work between the HIVIS website and Epicor.",
  },

  // ---- Current (September – October) ------------------------------------
  {
    id: "marketing-dashboard",
    name: "Marketing Dashboard",
    owners: ["Jordan"],
    startMonth: 9,
    endMonth: 10,
    category: "INTERNAL",
    status: "In Progress",
    description:
      "Create and maintain the annual marketing roadmap/dashboard for Sales and Management.",
  },
  {
    id: "catalogue-update",
    name: "Catalogue Update & Reprint",
    owners: ["Steve"],
    startMonth: 9,
    endMonth: 10,
    category: "CONTENT",
    status: "In Progress",
    description: "Review catalogue content, update pricing and prepare the next catalogue run.",
  },
  {
    id: "edm-campaign-process",
    name: "EDM Campaign Process",
    owners: ["Steve"],
    startMonth: 9,
    endMonth: 10,
    category: "PROCESS",
    status: "In Progress",
    description:
      "Create a visual process covering an EDM campaign from initial concept through to measurement and debrief.",
  },
  {
    id: "industry-edm",
    name: "Industry EDM Campaigns",
    owners: ["Jordan", "Steve"],
    startMonth: 9,
    endMonth: 10,
    category: "CAMPAIGN",
    status: "In Progress",
    description:
      "Develop industry-specific EDM campaigns and associated product content based around key HIVIS product groups.",
  },
  {
    id: "product-marketing-framework",
    name: "Product Marketing Framework",
    owners: ["Jordan"],
    startMonth: 9,
    endMonth: 10,
    category: "STRATEGY",
    status: "In Progress",
    description:
      "Define how HIVIS products should be marketed, including messaging, benefits and product positioning.",
  },
  {
    id: "hivis-direct-training",
    name: "HIVIS Direct Training",
    owners: ["Jordan"],
    startMonth: 9,
    endMonth: 10,
    category: "SALES SUPPORT",
    status: "In Progress",
    description:
      "Create training material to help Customer Service walk customers through HIVIS Direct from login through quoting and ordering.",
  },

  // ---- Upcoming (October onwards) ---------------------------------------
  {
    id: "flyers",
    name: "Flyers – Development & Design",
    owners: ["Steve"],
    startMonth: 10,
    endMonth: 12,
    category: "CONTENT",
    status: "Planned",
    description: "Develop and design upcoming HIVIS promotional and product flyers.",
  },
  {
    id: "mining-catalogue",
    name: "Mining Catalogue",
    owners: ["Steve"],
    startMonth: 10,
    endMonth: 12,
    category: "CONTENT",
    status: "Planned",
    description: "Develop and update the HIVIS Mining Catalogue.",
  },
  {
    id: "hivis-direct-promotion",
    name: "HIVIS Direct Promotion",
    owners: ["Steve"],
    startMonth: 10,
    endMonth: 11,
    category: "CAMPAIGN",
    status: "Planned",
    description: "Promote HIVIS Direct through EDMs, DL flyers and website content.",
  },
  {
    id: "click-collect-promotion",
    name: "Click & Collect Promotion",
    owners: ["Steve"],
    startMonth: 10,
    endMonth: 11,
    category: "CAMPAIGN",
    status: "Planned",
    description: "Promote Click & Collect through EDMs, DL flyers and website content.",
  },
  {
    id: "conference-lgp-iqa",
    name: "Conference Marketing – LGP & IQA",
    owners: [UNASSIGNED], // Owner not yet confirmed.
    startMonth: 10,
    endMonth: 10,
    category: "EVENTS",
    status: "Planned",
    description:
      "Prepare marketing collateral, printed material and video content for the LGP and IQA conferences.",
  },
];

/*
   Projects waiting on details. These are NOT shown on the roadmap.
   Once the owner and start/end months are confirmed, fill them in and move
   the entry into PROJECTS above.
*/
const PENDING_PROJECTS = [
  {
    id: "monthly-edm-reporting",
    name: "Monthly EDM & Reporting",
    owners: [], // TBC
    startMonth: null, // TBC
    endMonth: null, // TBC
    category: "CAMPAIGN", // Confirm
    status: "In Progress", // Confirm
    description: "", // TBC
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

/** Returns a 0-based month index from 1–12 or "SEP"-style input, or -1 if invalid. */
function monthIndex(value) {
  if (typeof value === "number") {
    return Number.isInteger(value) && value >= 1 && value <= 12 ? value - 1 : -1;
  }
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
  const validOwners = new Set([...TEAM, UNASSIGNED]);
  const seenIds = new Set();

  return projects.reduce((valid, raw, i) => {
    const start = monthIndex(raw.startMonth);
    const end = monthIndex(raw.endMonth);
    const owners = Array.isArray(raw.owners) ? raw.owners : [];
    const problems = [];

    if (!raw.id) problems.push("missing id");
    else if (seenIds.has(raw.id)) problems.push(`duplicate id "${raw.id}"`);
    if (!owners.length) problems.push("no owners");
    owners.filter((o) => !validOwners.has(o)).forEach((o) => problems.push(`unknown owner "${o}"`));
    if (start < 0) problems.push(`invalid startMonth "${raw.startMonth}"`);
    if (end < 0) problems.push(`invalid endMonth "${raw.endMonth}"`);
    if (start > end) problems.push("startMonth is after endMonth");
    if (!STATUS_CLASS[raw.status]) problems.push(`unknown status "${raw.status}"`);

    if (problems.length) {
      console.warn(`Roadmap: skipped project #${i + 1} "${raw.name}" – ${problems.join(", ")}`);
    } else {
      seenIds.add(raw.id);
      valid.push({ ...raw, owners, start, end, order: i });
    }
    return valid;
  }, []);
}

/**
 * Lane order: long-running / earlier-starting projects first, then current,
 * then upcoming. Ties (same start) put the longer project first, then keep
 * the order used in PROJECTS.
 */
function sortForLane(projects) {
  return [...projects].sort((a, b) => a.start - b.start || b.end - a.end || a.order - b.order);
}

function getCurrentMonth() {
  const configured = monthIndex(SITE_CONFIG.currentMonth);
  return configured >= 0 ? configured : new Date().getMonth();
}

/* ---------- Header + summary ---------- */

function renderHeader(projects) {
  document.getElementById("updated-label").textContent = SITE_CONFIG.updatedLabel;
  document.getElementById("roadmap-year").textContent = SITE_CONFIG.year;

  // Each project is one entry (even when shared), so this never double-counts.
  const activeCount = projects.filter((p) => p.status === "In Progress").length;

  const items = [
    { value: String(activeCount), label: `Active Project${activeCount === 1 ? "" : "s"}` },
    { value: String(TEAM.length), label: "Marketing Team Members" },
    { value: "Updated", label: SITE_CONFIG.updateFrequency },
  ];

  const summary = document.getElementById("summary");
  items.forEach((item) => {
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

/** "with Steve" / "with Jordan & Steve" for shared projects, from the lane owner's view. */
function sharedWith(project, laneOwner) {
  const others = project.owners.filter((o) => o !== laneOwner && o !== UNASSIGNED);
  return others.length ? `with ${others.join(" & ")}` : "";
}

function renderBar(project, rowIndex, laneOwner) {
  const span = project.end - project.start + 1;
  const statusClass = STATUS_CLASS[project.status];
  // A div (not <button>) so the label can stay sticky while scrolling; keyboard
  // support is added in setupPopover.
  const bar = el("div", `bar bar--${statusClass}${span === 1 ? " bar--short" : ""}`);
  bar.setAttribute("role", "button");
  bar.tabIndex = 0;
  bar.dataset.projectId = project.id;
  bar.dataset.lane = laneOwner;

  // Position and width come straight from the month numbers on the 12-column grid.
  bar.style.gridColumn = `${project.start + 1} / span ${span}`;
  bar.style.gridRow = String(rowIndex + 1);

  const shared = sharedWith(project, laneOwner);
  bar.setAttribute(
    "aria-label",
    [project.name, project.category, project.status, formatTiming(project), shared].filter(Boolean).join(", ")
  );

  const meta = el("span", "bar-category");
  meta.append(document.createTextNode(project.category));
  if (shared) meta.append(el("span", "bar-shared", ` · ${shared}`));

  const dot = el("span", `status-dot status-dot--${statusClass}`);
  dot.title = project.status;

  bar.append(el("span", "bar-name", project.name), meta, dot);
  return bar;
}

function renderLane(lane, projects, currentMonth) {
  const row = el("div", `roadmap-row lane${lane.understated ? " lane--understated" : ""}`);
  row.setAttribute("role", "row");

  // Sticky name column
  const label = el("div", "lane-label");
  label.setAttribute("role", "rowheader");
  label.append(el("span", "lane-name", lane.label));
  const count = projects.length;
  label.append(el("span", "lane-count", count ? `${count} project${count === 1 ? "" : "s"}` : "No active projects"));
  row.append(label);

  // Track: one project per row, so each lane grows to fit its own projects.
  const track = el("div", "lane-track");
  track.setAttribute("role", "cell");
  const ordered = sortForLane(projects);
  track.style.gridTemplateRows = `repeat(${Math.max(ordered.length, 1)}, auto)`;

  // Month guides + current month highlight sit behind the bars.
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
    ordered.forEach((project, r) => track.append(renderBar(project, r, lane.owner)));
  }

  row.append(track);
  return row;
}

function renderRoadmap(projects) {
  const roadmap = document.getElementById("roadmap");
  const currentMonth = getCurrentMonth();
  const inLane = (owner) => projects.filter((p) => p.owners.includes(owner));

  roadmap.append(renderMonthHeader(currentMonth));

  TEAM.forEach((name) => {
    roadmap.append(renderLane({ owner: name, label: name }, inLane(name), currentMonth));
  });

  // Understated lane for projects without a confirmed owner; hidden when empty.
  const unassigned = inLane(UNASSIGNED);
  if (unassigned.length) {
    roadmap.append(
      renderLane({ owner: UNASSIGNED, label: UNASSIGNED_LANE_LABEL, understated: true }, unassigned, currentMonth)
    );
  }

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
  const popover = document.getElementById("popover");
  const roadmap = document.getElementById("roadmap");
  const scroller = document.getElementById("roadmap-scroll");

  let activeBar = null;
  let pinned = false;
  let suppressFocusPreview = false; // avoids re-opening when focus returns after closing

  function fill(project) {
    document.getElementById("popover-category").textContent = project.category;
    document.getElementById("popover-title").textContent = project.name;
    document.getElementById("popover-owner-label").textContent = project.owners.length > 1 ? "Owners" : "Owner";
    document.getElementById("popover-owner").textContent = project.owners.join(" & ");
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

  // Enter / Space act like a click, as on a native button
  roadmap.addEventListener("keydown", (e) => {
    const bar = e.target.closest(".bar");
    if (bar && (e.key === "Enter" || e.key === " ")) {
      e.preventDefault();
      bar.click();
    }
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
  renderHeader(projects);
  renderRoadmap(projects);
  setupPopover(projects);
});
