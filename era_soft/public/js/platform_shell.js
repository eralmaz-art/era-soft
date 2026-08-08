(() => {
	if (window.eraPlatformCommandCenterInitialized) {
		return;
	}
	window.eraPlatformCommandCenterInitialized = true;

	const PLATFORM_ROUTE = "Workspaces/ERA SOFT";
	const MAX_RENDER_ATTEMPTS = 20;

	function is_platform_route() {
		return document.body.dataset.route === PLATFORM_ROUTE;
	}

	function capitalize(value) {
		return value ? value.charAt(0).toUpperCase() + value.slice(1) : value;
	}

	function get_first_name() {
		const boot_user = frappe.boot?.user || {};
		const full_name =
			boot_user.first_name ||
			boot_user.full_name ||
			frappe.session?.user_fullname ||
			frappe.session?.user;
		const first_name = (full_name || "").trim().split(/\s+/)[0];

		return !first_name || first_name === "Administrator" ? "Алмаз" : first_name;
	}

	function get_company() {
		return (
			frappe.defaults?.get_default?.("company") ||
			frappe.boot?.sysdefaults?.company ||
			"ERA Group"
		);
	}

	function get_greeting(hour) {
		if (hour < 5) return "Доброй ночи";
		if (hour < 12) return "Доброе утро";
		if (hour < 18) return "Добрый день";
		return "Добрый вечер";
	}

	function command_center_markup() {
		return `
			<section class="era-command-center" aria-label="Центр управления ERA SOFT">
				<div class="era-command-center__top">
					<div class="era-command-center__welcome">
						<span class="era-command-center__product">ERA SOFT · Business Operating Platform</span>
						<h1><span data-era-greeting>Доброе утро</span>, <span data-era-first-name>Алмаз</span>.</h1>
						<div class="era-command-center__date">
							<span data-era-weekday>Пятница</span>
							<span aria-hidden="true">·</span>
							<span data-era-date>08 августа</span>
							<span aria-hidden="true">·</span>
							<time data-era-time>08:30</time>
						</div>
					</div>
					<details class="era-company-context">
						<summary>
							<span>Компания</span>
							<strong data-era-company>ERA Group</strong>
							<span class="era-company-context__chevron" aria-hidden="true">⌄</span>
						</summary>
						<div class="era-company-context__menu">
							<strong data-era-company-menu>ERA Group</strong>
							<small>Текущий контекст</small>
						</div>
					</details>
				</div>
				<div class="era-command-center__mission">
					<span>One Platform.</span>
					<strong>Many Businesses.</strong>
					<small>Building better businesses with trusted data.</small>
				</div>
				<nav class="era-command-center__actions" aria-label="Быстрые действия">
					<button type="button" data-era-action="search"><span aria-hidden="true">⌕</span> Поиск</button>
					<button type="button" data-era-action="recent"><span aria-hidden="true">↺</span> Последние действия</button>
					<button type="button" data-era-action="notifications"><span aria-hidden="true">○</span> Уведомления</button>
				</nav>
			</section>`;
	}

	function owner_priority_markup() {
		return `
			<section class="era-owner-priority" aria-labelledby="era-owner-priority-title">
				<div class="era-owner-priority__label">Главный инструмент собственника</div>
				<a class="era-owner-priority__card" href="/desk/dashboard">
					<span class="era-owner-priority__icon" aria-hidden="true">📊</span>
					<span class="era-owner-priority__body">
						<span id="era-owner-priority-title">Панель руководителя</span>
						<span>Деньги, проекты, события и риски в одном обзоре</span>
					</span>
					<span class="era-platform-status">Основа готова</span>
					<span class="era-owner-priority__arrow" aria-hidden="true">→</span>
				</a>
			</section>`;
	}

	function construction_card_markup() {
		return `
			<span class="era-platform-app__icon" aria-hidden="true">🏗</span>
			<span class="era-platform-app__body">
				<span class="era-platform-app__heading">
					<span class="era-platform-app__name">ERA Construction</span>
					<span class="era-platform-status">Активно</span>
				</span>
				<span class="era-platform-app__description">Основное рабочее приложение ERA SOFT</span>
				<span class="era-construction-metrics">
					<span><small>Версия</small><strong>0.5</strong></span>
					<span><small>Последнее обновление</small><strong>Сегодня</strong></span>
					<span><small>Модулей готово</small><strong>2 из 7</strong></span>
				</span>
			</span>`;
	}

	function update_dynamic_content(command_center) {
		const now = new Date();
		const weekday = capitalize(
			new Intl.DateTimeFormat("ru-RU", { weekday: "long" }).format(now)
		);
		const date = new Intl.DateTimeFormat("ru-RU", {
			day: "2-digit",
			month: "long",
		}).format(now);
		const time = new Intl.DateTimeFormat("ru-RU", {
			hour: "2-digit",
			minute: "2-digit",
			hour12: false,
		}).format(now);
		const company = get_company();

		command_center.querySelector("[data-era-greeting]").textContent = get_greeting(now.getHours());
		command_center.querySelector("[data-era-first-name]").textContent = get_first_name();
		command_center.querySelector("[data-era-weekday]").textContent = weekday;
		command_center.querySelector("[data-era-date]").textContent = date;
		command_center.querySelector("[data-era-time]").textContent = time;
		command_center.querySelector("[data-era-company]").textContent = company;
		command_center.querySelector("[data-era-company-menu]").textContent = company;
	}

	function hide_source_heading(editor) {
		for (const block of editor.querySelectorAll(".ce-block")) {
			const text = block.textContent.trim();
			if (text === "ERA SOFT" || text === "Операционная платформа для бизнеса") {
				block.hidden = true;
			}
		}
	}

	function enhance_application_cards(editor) {
		const construction = editor.querySelector(
			'.era-platform-grid--apps a[href="/desk/construction"]'
		);
		if (construction && !construction.classList.contains("era-platform-app--construction")) {
			construction.classList.add("era-platform-app--construction");
			construction.innerHTML = construction_card_markup();
		}

		const concrete = editor.querySelector('.era-platform-grid--apps a[href="/desk/era-concrete"]');
		if (concrete) {
			const status = concrete.querySelector(".era-platform-status");
			const description = concrete.querySelector(".era-platform-app__description");
			if (status) status.textContent = "Старт после Construction MVP";
			if (description) description.textContent = "Следующий продукт платформы";
		}

		const original_dashboard = editor.querySelector(
			'.era-platform-grid--management a[href="/desk/dashboard"]'
		);
		original_dashboard?.remove();
	}

	function enhance_platform_shell(attempt = 0) {
		if (!is_platform_route()) return;

		const editor = document.querySelector(".layout-main-section .codex-editor__redactor");
		if (!editor) {
			if (attempt < MAX_RENDER_ATTEMPTS) {
				window.setTimeout(() => enhance_platform_shell(attempt + 1), 100);
			}
			return;
		}

		hide_source_heading(editor);

		let command_center = editor.querySelector(".era-command-center");
		if (!command_center) {
			editor.insertAdjacentHTML("afterbegin", command_center_markup());
			command_center = editor.querySelector(".era-command-center");
		}

		if (!editor.querySelector(".era-owner-priority")) {
			command_center.insertAdjacentHTML("afterend", owner_priority_markup());
		}

		update_dynamic_content(command_center);
		enhance_application_cards(editor);
	}

	function click_sidebar_control(selector) {
		const control = document.querySelector(selector);
		if (control) {
			control.click();
			return;
		}
		frappe.show_alert({ message: "Элемент управления недоступен", indicator: "orange" });
	}

	document.addEventListener("click", (event) => {
		const action = event.target.closest("[data-era-action]")?.dataset.eraAction;
		if (!action) return;

		if (action === "notifications") {
			click_sidebar_control(".sidebar-notification");
			return;
		}
		click_sidebar_control("#navbar-modal-search, .navbar-modal-search-mobile");
	});

	frappe.router.on("change", () => enhance_platform_shell());
	$(document).on("page-change", () => enhance_platform_shell());
	window.setInterval(() => {
		const command_center = document.querySelector(".era-command-center");
		if (is_platform_route() && command_center) update_dynamic_content(command_center);
	}, 60_000);
	enhance_platform_shell();
})();
