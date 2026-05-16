const languageButton = document.querySelector("[data-language-toggle]");
const fontButton = document.querySelector("[data-font-toggle]");
const translatableElements = document.querySelectorAll("[data-ja][data-en]");

const state = {
  language: localStorage.getItem("site-language") || "ja",
  fontLarge: localStorage.getItem("site-font") === "large",
};

function applyLanguage(language) {
  document.documentElement.lang = language;
  translatableElements.forEach((element) => {
    const value = element.dataset[language];
    if (!value) return;

    if (element instanceof HTMLInputElement || element instanceof HTMLTextAreaElement) {
      element.placeholder = value;
      return;
    }

    element.textContent = value;
  });

  document.title =
    language === "ja"
      ? "知足湧生メディカルセンター | 架空医療機関ポートフォリオサイト"
      : "Chisoku Yusei Medical Center | Fictional Healthcare Portfolio Site";

  const description = document.querySelector('meta[name="description"]');
  if (description) {
    description.content =
      language === "ja"
        ? "知足湧生メディカルセンターは、地域医療・入院支援・採用情報・会計案内・診療担当医・お知らせを掲載した架空医療機関のポートフォリオサイトです。"
        : "Chisoku Yusei Medical Center is a fictional healthcare portfolio website with patient guides, careers, billing, doctor schedules, blog posts, and news.";
  }

  languageButton.setAttribute("aria-pressed", String(language === "en"));
  localStorage.setItem("site-language", language);
}

function applyFontSize(isLarge) {
  document.body.classList.toggle("font-large", isLarge);
  fontButton.setAttribute("aria-pressed", String(isLarge));
  localStorage.setItem("site-font", isLarge ? "large" : "default");
}

languageButton.addEventListener("click", () => {
  state.language = state.language === "ja" ? "en" : "ja";
  applyLanguage(state.language);
});

fontButton.addEventListener("click", () => {
  state.fontLarge = !state.fontLarge;
  applyFontSize(state.fontLarge);
});

document.querySelector(".contact-form")?.addEventListener("submit", (event) => {
  event.preventDefault();
  const note = event.currentTarget.querySelector(".form-note");
  if (!note) return;
  note.textContent =
    state.language === "ja"
      ? "送信デモです。実際の送信処理は行われません。"
      : "Demo only. No message has been submitted.";
});

applyLanguage(state.language);
applyFontSize(state.fontLarge);
