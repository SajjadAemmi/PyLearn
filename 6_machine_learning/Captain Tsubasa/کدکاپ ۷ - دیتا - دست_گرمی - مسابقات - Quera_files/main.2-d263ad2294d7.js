document.addEventListener("DOMContentLoaded", () => {
  if ("moment" in window)
    moment.loadPersian({
      usePersianDigits: true,
      dialect: "persian-modern",
    });
});

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

$.ajaxSetup({
  beforeSend(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie("csrf_token"));
    }
  },
});

function init_semantic() {
  $(".qu-dropdown").each((i, e) => {
    const settings = {
      fullTextSearch: true,
      forceSelection: false,
      selectOnKeydown: false, // a11y
    };
    if ($(e).hasClass("clearable")) settings.clearable = true;
    $(e).dropdown(settings);
  });
  $(".qu-checkbox").checkbox();
  $(".menu .item").tab();
  // $('.menu .item').tab({
  //    history: true,
  //    historyType: 'hash'
  // });
  $(".qu-popup").popup();
  $(".qu-accordion").accordion();
}

function staticfiles(url) {
  return `/static/${url}`;
}

// https://remysharp.com/2010/07/21/throttling-function-calls
function quera_debounce(fn, delay) {
  let timer = null;
  return function () {
    const context = this;
    const args = arguments;
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(context, args);
    }, delay);
  };
}

const englishDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const persianDigits = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];

function persian_digits(str) {
  return str.toString().replace(/\d/g, (d) => persianDigits[Number(d)]);
}

function persian_float(s) {
  return persian_digits(s).replace(".", "٫");
}

function english_digits(str) {
  return str.toString().replace(/[۰۱۲۳۴۵۶۷۸۹]/g, (d) => englishDigits[persianDigits.indexOf(d)]);
}

function price_with_comma(str) {
  return str.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function persian_comma(str) {
  return str.toString().replace(",", "٬");
}

function persian_price_with_comma(str) {
  str = price_with_comma(str);
  str = persian_digits(str);
  str = persian_comma(str);
  return str;
}

function humanize_number(number) {
  let value = number.toString();
  const value_splitted = value.split(/(?=(?:...)*$)/);
  value = value_splitted.join(",");
  return value;
}

function html_escape(value) {
  return $("<div/>").text(value).html();
}

// selectText is used for "Select All" when viewing a submitted code
jQuery.fn.selectText = function () {
  const doc = document;
  const element = this[0];
  let range;
  let selection;
  if (doc.body.createTextRange) {
    range = document.body.createTextRange();
    range.moveToElementText(element);
    range.select();
  } else if (window.getSelection) {
    selection = window.getSelection();
    range = document.createRange();
    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
  }
};

function s_humanize(s) {
  s = ~~(s / 60);
  let h = ~~(s / 60);
  let m = s % 60;
  if (h < 10) h = `0${h}`;
  if (m < 10) m = `0${m}`;
  return persian_digits(`${h}:${m}`);
}

function duration_nice_repr(duration) {
  // Gets moment.duration objects
  const result = [];
  if (duration.years() > 0) result.push(`${persian_digits(duration.years())} سال`);
  if (duration.months() > 0) result.push(`${persian_digits(duration.months())} ماه`);
  if (duration.days() > 0) result.push(`${persian_digits(duration.days())} روز`);
  if (duration.hours() > 0) result.push(`${persian_digits(duration.hours())} ساعت`);
  if (duration.minutes() > 0) result.push(`${persian_digits(duration.minutes())} دقیقه`);
  if (duration.seconds() > 0) result.push(`${persian_digits(duration.seconds())} ثانیه`);
  let result_str = "";
  for (let i = 0; i < result.length; i++) {
    result_str += result[i];
    if (i != result.length - 1) result_str += " و ";
  }
  return result_str;
}

Noty.overrideDefaults({
  layout: "bottomLeft",
  theme: "relax",
  type: "info",
  animation: {
    open: "noty_effects_open",
    close: "noty_effects_close",
  },
  timeout: 3000,
  closeWith: ["click"],
});

$(document).ready(() => {
  init_semantic();

  const mobile_menu_toggle_button = $("#mobile-menu-toggle");
  if (mobile_menu_toggle_button.length) {
    // if toggle button exists
    const toggle_icon = mobile_menu_toggle_button.children(".icon");

    function toggleMenu() {
      $("#mobile-menu").transition({
        animation: "slide down",
        onStart() {
          if (toggle_icon.attr("class") === "large arrow left icon") {
            toggle_icon.attr("class", "large sidebar icon");
            $("#mobile-menu-overlay").remove();
          } else {
            toggle_icon.attr("class", "large arrow left icon");
            $("#quera-base-container, #land-body").append('<div id="mobile-menu-overlay"></div>');
          }
        },
      });
    }

    mobile_menu_toggle_button.click((e) => {
      e.preventDefault();
      toggleMenu();
    });
    $("#quera-base-container, #land-body").on("click", "#mobile-menu-overlay", toggleMenu);
  }
});

// https://varvy.com/pagespeed/defer-images.html
function defer_load_images() {
  const imgDefer = document.getElementsByTagName("img");
  for (let i = 0; i < imgDefer.length; i++) {
    if (imgDefer[i].getAttribute("data-src") && !imgDefer[i].getAttribute("data-load-on-visibility")) {
      imgDefer[i].setAttribute("src", imgDefer[i].getAttribute("data-src"));
    }
  }
}

document.addEventListener("DOMContentLoaded", defer_load_images);

document.addEventListener("DOMContentLoaded", () => {
  $(".qrate-progress").each((i, e) => {
    const circle = new ProgressBar.Circle(e, {
      color: "#00b5ad",
      duration: 1400,
      easing: "easeInOut",
      strokeWidth: 6,
      trailWidth: 2,
    });
    circle.animate(($(e).data("rate") / 10) * 0.9 + 0.1);
  });
});

function setPopup(cssSelector, hoverContent, clickContent) {
  const element = $(cssSelector);
  element.on("mouseenter", () => {
    element.popup({ content: hoverContent, on: "manual" }).popup("show");
  });
  element.on("mouseleave", () => {
    element.popup("hide");
  });
  element.on("click", () => {
    element.popup({ content: clickContent, on: "manual" }).popup("show");
  });
}

function createGoogleCalenderURL({ title, details, isOnline, startTime, finishTime }) {
  const jsStartTime = moment(startTime);

  let jsFinishTime;
  if (finishTime) jsFinishTime = moment(finishTime);

  const baseGoogleCalendarUrl = "https://calendar.google.com/calendar/r/eventedit?";
  const datetimeFormat = "YYYYMMDDTHH:mm:ssZ";
  const startTimeParameter = english_digits(`${jsStartTime.format(datetimeFormat)}`);
  const startTimeWithZBeforeMinus = startTimeParameter.replace(/[-]/g, "Z-");
  const startTimeWithZBeforeMinusPlus = startTimeWithZBeforeMinus.replace(/[+]/g, "Z+");
  const finishTimeParameter = finishTime ? english_digits(`/${jsFinishTime.format(datetimeFormat)}`) : "";
  const finishTimeWithZBeforeMinus = finishTimeParameter.replace(/[-]/g, "Z-");
  const finishTimeWithZBeforeMinusPlus = finishTimeWithZBeforeMinus.replace(/[+]/g, "Z+");

  const calendarLink =
    `${baseGoogleCalendarUrl}` +
    `&text=${title}` +
    `&dates=${startTimeWithZBeforeMinusPlus}${finishTimeWithZBeforeMinusPlus}` +
    `&details=${details}`;

  const spacelessCalendarLink = calendarLink.replace(/ /g, "%20");
  let calendarLinkWithOnlineLocation;
  if (isOnline) {
    calendarLinkWithOnlineLocation = `${spacelessCalendarLink}&location=Online`;
  }

  return calendarLinkWithOnlineLocation || spacelessCalendarLink;
}
