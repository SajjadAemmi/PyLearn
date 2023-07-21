const fileExtensions = {
  git: "git",
  file: "file",
  perl: "perl",
  php: "php",
  cpp: "cpp",
  babel: "babel",
  js: "javascript",
  javascript: "javascript",
  eslint: "eslint",
  typescript: "typescript",
  react_ts: "react_ts",
  html: "html",
  readme: "readme",
  scala: "scala",
  py: "python",
  python: "python",
  django: "django",
  docker: "docker",
  "python-misc": "python-misc",
  npm: "npm",
  java: "java",
  md: "markdown",
  yaml: "yaml",
  dart: "dart",
  elixir: "elixir",
  cobol: "cobol",
  ruby: "ruby",
  rust: "rust",
  xml: "xml",
  go: "go_gopher",
  c: "c",
  haskell: "haskell",
  clojure: "clojure",
  react: "react",
  css: "css",
  laravel: "laravel",
  sh: "bash",
  bash: "bash",
  terminal: "terminal",
  jsx: "react",
};

function getIcon(name) {
  return staticfiles(`images/icons/extensions/${fileExtensions[name] ?? fileExtensions.file}.svg`);
}

const escapeTest = /[&<>"']/;
const escapeReplace = /[&<>"']/g;
const escapeTestNoEncode = /[<>"']|&(?!#?\w+;)/;
const escapeReplaceNoEncode = /[<>"']|&(?!#?\w+;)/g;
const escapeReplacements = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;",
};
const getEscapeReplacement = (ch) => escapeReplacements[ch];

function escapeHtml(html, encode) {
  if (encode) {
    if (escapeTest.test(html)) {
      return html.replace(escapeReplace, getEscapeReplacement);
    }
  } else if (escapeTestNoEncode.test(html)) {
    return html.replace(escapeReplaceNoEncode, getEscapeReplacement);
  }

  return html;
}

function render_markdown(md_text, result_html_div = null, markedOptions = {}) {
  /*
    if (result_html_div is null) this function returns result html as text
    else this function render markdown in result_html_div
        example 1:
            html_div.html(render_markdown(md_text))
        example 2:
            render_markdown(md_text, html_div)
    */
  const mapping_katex = [];

  function katex_step1(text) {
    const mapping_code = [];
    // 1. replace inline codes (`code`) with placeholders (to let KaTeX do its work without problem)
    text = text.replace(/(`+)\s*([\s\S]*?[^`])\s*\1(?!`)/g, (match) => {
      const placeholder = `qcodeph${Math.floor(Math.random() * 1000000 + 1)}`;
      mapping_code.push([placeholder, match]);
      return placeholder;
    });
    // 2. let KaTeX do its work
    const element = $("<div/>").html(text);
    try {
      renderMathInElement(element[0], {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "\\[", right: "\\]", display: true },
          { left: "\\(", right: "\\)", display: false },
          { left: "$", right: "$", display: false },
        ],
      });
    } catch (e) {
      console.log(e);
    }
    // 3. Replace KaTeX html elements with placeholders (to let marked.js do its work without problem)
    element.children().each((i, e) => {
      const placeholder = `qkatexph${Math.floor(Math.random() * 1000000 + 1)}`;
      mapping_katex.push([placeholder, $(e).prop("outerHTML")]);
      $(e).replaceWith(placeholder);
    });
    text = element.html();
    // 4. Restore inline code placeholders with real codes
    // https://stackoverflow.com/a/40005925/1744633
    for (let i = 0; i < mapping_code.length; i++) text = text.replace(mapping_code[i][0], () => mapping_code[i][1]);
    return text;
  }

  function katex_step2(text) {
    // replace katex placeholders with KaTeX html elements
    // https://stackoverflow.com/a/40005925/1744633
    for (let i = 0; i < mapping_katex.length; i++) text = text.replace(mapping_katex[i][0], () => mapping_katex[i][1]);
    return text;
  }

  function customTokenExtractor(tokens) {
    // "[^]" is used instead of "." with s (dotall) flag. "[^]" matches any character including newline
    // reason: s flag is not supported in FireFox

    const customTags = [
      { type: "paragraph", regex: /((?:^|\n)&lt;summary&gt;[^]*?&lt;\/summary&gt;)/ },
      {
        type: "paragraph",
        regex: /((?:^|\n)&lt;(?:details\s*(?:(?: class=".*?")?(?: open)?|(?: open)?(?: class=".*?")?)|\/details)&gt;)/,
      },
      {
        type: "paragraph",
        regex: /(%align_(?:center|left|right)_start%)/,
      },
    ];

    const convertRegexToTag = (customTag, tokens) => {
      const newTokens = marked.lexer("");

      tokens.forEach((token) => {
        if (token.type === customTag.type) {
          token.text
            .split(customTag.regex)
            .map((c) => c.trim())
            .filter((c) => c.length > 0)
            .forEach((c) => newTokens.push({ type: "paragraph", text: c }));
        } else {
          newTokens.push(token);
        }
      });

      return newTokens;
    };

    let newTokens = tokens;
    customTags.forEach((customTag) => {
      newTokens = convertRegexToTag(customTag, newTokens);
    });

    return newTokens;
  }

  function tagReplacer(text) {
    // "[^]" is used instead of "." with s (dotall) flag. "[^]" matches any character including newline
    // reason: s flag is not supported in FireFox
    return text
      .replace(/<p>\s*&lt;summary&gt;([^]*?)&lt;\/summary&gt;\s*<\/p>/g, "<summary>$1</summary>")
      .replace(/<p>\s*&lt;details&gt;\s*<\/p>/g, "<details>")
      .replace(/<p>\s*&lt;details\s*(?: class=&quot;(.+?)&quot;)?\s*( open)?\s*&gt;\s*<\/p>/g, '<details class="$1"$2>')
      .replace(/<p>\s*&lt;details\s*( open)?\s*(?: class=&quot;(.+?)&quot;)?\s*&gt;\s*<\/p>/g, '<details class="$2"$1>')
      .replace(/<p>\s*&lt;\/details&gt;\s*<\/p>/g, "</details>")
      .replace(/<p>\s*%align_(center|left|right)_start%\s*<\/p>/g, '<div class="align-$1">')
      .replace(/<p>\s*%align_end%\s*<\/p>/g, "</div>");
  }

  function convert_js_markdown_variables(markdown_text, use_placeholder) {
    const meet_skyroom_replacement_div = `
            <div id="skyroom_dark_bg"
                  style="display: none; position: fixed; padding: 0; z-index: 1001; width: 100%; height: 100%;
                        right: 0; bottom: 0; background-color: black; opacity: 0.8;"
            >
            </div>
            <div id="skyroom_$1" style="height: 350px; direction: rtl">
                <div style="position: absolute; background-color: #eeeeee; display: flex; padding: 5px 10px; border-radius: 0 0 0 10px;">
                    <a id="skyroom-newtab" data-tooltip="تب جدید" data-position="top center" onclick="minimize()"
                        target="_blank" rel="noopener noreferrer" href="https://www.skyroom.online/ch/$1"
                        style="display: inline-flex;">
                        <i class="external square alternate link icon qu-popup"></i>
                    </a>
                    <div id="maximize-icon" data-tooltip="بزرگ‌نمایی" data-position="top center"
                        onclick="maximize()" style="display: inline-flex">
                        <i class="window maximize outline link icon qu-popup"></i>
                    </div>
                    <div id="minimize-icon" data-tooltip="کوچک‌نمایی" data-position="bottom center"
                        onclick="minimize()" style="display: none">
                        <i class="window minimize outline link icon qu-popup"></i>
                    </div>
                </div>
                <iframe src="https://www.skyroom.online/ch/$1"
                    width="100%" height="100%" frameborder="0" allowFullScreen="true"
                    allow="autoplay;fullscreen;speaker;microphone;camera;display-capture">
                </iframe>
                <script>
                    function maximize() {
                        document.getElementById("skyroom_dark_bg").style.display = "block";
                        document.getElementById("skyroom-newtab").setAttribute("data-position", "bottom center");
                        document.getElementById("skyroom_$1")
                            .setAttribute(
                                "style",
                                "position: fixed; display: block; width: 100%; height: 100%; right: 0px; padding: 30px; bottom: 0px; z-index: 1002; direction: rtl;"
                            );
                        document.getElementById("maximize-icon").setAttribute("style", "display: none");
                        document.getElementById("minimize-icon").setAttribute("style", "display: inline-flex");
                        document.getElementsByTagName("body")[0].setAttribute("style", "overflow: hidden;");
                    }
                    function minimize() {
                        document.getElementById("skyroom_dark_bg").style.display = "none";
                        document.getElementById("skyroom-newtab").setAttribute("data-position", "top center");
                        document.getElementById("skyroom_$1")
                            .setAttribute("style", "height: 350px; direction: rtl");
                        document.getElementById("maximize-icon").setAttribute("style", "display: inline-flex");
                        document.getElementById("minimize-icon").setAttribute("style", "display: none");
                        document.getElementsByTagName("body")[0].setAttribute("style", "");
                    }
                </script>
            </div>
        `;
    const patterns_and_replacements = [
      {
        pattern: /%video.aparat_([a-zA-Z0-9]*)%/g,
        replacement:
          '<div id="$1"><script type="text/JavaScript" src="https://www.aparat.com/embed/$1?data[rnddiv]=$1&data[responsive]=yes"></script></div>',
        placeholder: "**aparat_video_goes_here**",
      },
      {
        // Example: https://player.arvancloud.com/index.html?config=https://channelname.arvanvod.com/VbKw5Bvn0r/1d72f7097e086007769e34007b27e20f/1590579907/YjA9za1xpM/origin_config.json?secure=true
        pattern: /%video.arvan_((https:\/\/player\.arvancloud\.com\/index\.html\?config=https:\/\/[-a-zA-Z0-9@:%._\+~#=]+\.arvanvod\.com\/[a-zA-Z0-9()/_.?=]+))%/g,
        replacement:
          '<div class="arvan_iframe_embed"> <iframe src="$1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowFullScreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe> </div>',
        placeholder: "**arvan_video_goes_here**",
      },
      {
        pattern: /%meet.skyroom_(.+)%/g,
        replacement: meet_skyroom_replacement_div,
        placeholder: "**skyroom_video_goes_here**",
      },
    ];
    patterns_and_replacements.forEach((pattern_and_replacement) => {
      const { pattern } = pattern_and_replacement;

      let replacement;
      if (use_placeholder) {
        replacement = pattern_and_replacement.placeholder;
      } else replacement = pattern_and_replacement.replacement;

      markdown_text = markdown_text.replace(pattern, replacement);
    });
    return markdown_text;
  }

  // customize renderer (to disable id from headings)
  const renderer = new marked.Renderer();

  renderer.code = (text, params = "") => {
    const [language, filename, extension] = params.split(" ");
    if (language === "jupyter") {
      try {
        return renderJupyterJson(JSON.parse(text));
      } catch (e) {
        return e.toString();
      }
    }

    let filenameEl;
    if (filename) {
      const [, extensionFromName] = filename.split(".");
      const icon = getIcon(extension ?? extensionFromName);
      filenameEl = `<div class="filename"><img class="skip-modal" alt="extensionFromName" src="${icon}"/>${filename}</div>`;
    }
    return `${filename ? filenameEl : ""}<pre class="code-block"><code data-filename="${filename}" class="${
      language ? `language-${language}` : ""
    }">${escapeHtml(text, true)}</code></pre>`;
  };

  marked.setOptions({
    // renderer: renderer,
    headerIds: false,
    gfm: true,
    tables: true,
    smartLists: true,
    sanitize: true, // Actually, doesn't matter!
    placeholder: false,
    renderer,
    ...markedOptions,
  });

  let html_div = $("<div></div>");
  if (result_html_div != null) html_div = result_html_div;
  // Replace occurrences of &gt; at the beginning of a new line with ">"
  // so Markdown blockquotes are handled correctly
  md_text = md_text.replace(/^&gt;/gm, ">");

  // Tokenize
  let tokens = marked.lexer(md_text);

  // Extract <details>, <summary> tags as separate tokens
  tokens = customTokenExtractor(tokens);

  // Run katex_step1 on token texts (except for code blocks)
  for (let i = 0; i < tokens.length; i++) {
    const token = tokens[i];
    switch (token.type) {
      case "heading":
      case "paragraph":
      case "text":
        token.text = katex_step1(token.text);
        break;
      case "table":
        for (let j = 0; j < token.header.length; j++) {
          token.header[j] = katex_step1(token.header[j]);
        }
        for (let j = 0; j < token.cells.length; j++)
          for (let k = 0; k < token.cells[j].length; k++) token.cells[j][k] = katex_step1(token.cells[j][k]);
        break;
    }
  }
  tokens.forEach((token) => {});

  // Let marked.js parse tokens
  let marked_text = marked.parser(tokens);

  // Run katex_step2 on parsed output
  marked_text = katex_step2(marked_text);

  // Replace <details>, <summary> placeholders with real tags
  marked_text = tagReplacer(marked_text);

  // Replace videos embed
  marked_text = convert_js_markdown_variables(marked_text, markedOptions.placeholder);

  // Show the result
  html_div.html(marked_text);

  // Set elements' text directions
  html_div
    .children()
    .attr(
      "dir",
      "auto",
    ); /*
    if (result_html_div is null) this function returns result html as text
    else this function render markdown in result_html_div
        example 1:
            html_div.html(render_markdown(md_text))
        example 2:
            render_markdown(md_text, html_div)
    */

  html_div.find("a").attr("target", "_blank");

  html_div.find("details").children().attr("dir", "auto");
  html_div.find("img:not(.skip-modal)").css("cursor", "pointer");
  html_div.find("img:not(.skip-modal)").click((e) => {
    const img = e;
    $("#img-modal")
      .modal({
        close: ".close.icon",
        onShow() {
          $("#img-modal img").attr("src", img.target.src);
        },
      })
      .modal("show");
  });

  html_div.append(`<div class="ui basic modal" id="img-modal">
            <div class="image content" style="justify-content: center; align-items: center">
                <img class="image" style="max-width: 100%" src=""/>
            </div>
        </div>`);
  // We needed to change auto to ltr, because of Edge browser
  // html_div.find('pre').attr('dir', 'auto');
  html_div.find("pre").attr("dir", "ltr");

  html_div.find("code").each((i, e) => {
    if (!$(e).parent().is("pre"))
      // set direction for inline codes
      // We needed to change auto to ltr, because of Edge browser
      // $(e).attr('dir', 'auto');
      $(e).attr("dir", "ltr");
    // Fix Code Blocks (un-escape inner html)
    // and enable <mark> tags
    $(e).html(
      $(e)
        .text()
        .replace(
          /&lt;mark\s*( title="[^"]*?")?\s*( class="(?:red|orange|yellow|olive|green|teal|blue|violet|purple|pink|brown|grey)")?\s*&gt;(.*?)&lt;\/mark&gt;/g,
          "<mark$1$2>$3</mark>",
        )
        .replace(
          /&lt;mark\s*( class="(?:red|orange|yellow|olive|green|teal|blue|violet|purple|pink|brown|grey)")?\s*( title="[^"]*?")?\s*&gt;(.*?)&lt;\/mark&gt;/g,
          "<mark$1$2>$3</mark>",
        ),
    );
  });

  // add semantic-ui class to tables
  html_div.find("table").addClass("ui unstackable table");

  // Syntax Highlight Codes
  html_div
    .find("pre code")
    .filter(function () {
      return this.className.match(/language-.*/);
    })
    .each((i, e) => {
      // enable line numbers
      e.parentElement.className += " line-numbers";
      Prism.highlightElement(e);
    });

  // Enable "Copy" button for simple code elements
  html_div
    .find("pre code")
    .filter(function () {
      return !this.className.match(/language-.*/);
    })
    .each((i, e) => {
      Prism.highlightElement(e);
    });

  html_div.find("mark[title]").each(function (i, e) {
    $(e).popup({
      content: this.title,
      position: "top center",
      variation: "small",
    });
    $(this).removeAttr("title");
  });

  html_div.find("h1,h2,h3,h4,h5,h6").each((i, heading) => {
    const $heading = $(heading);
    const headingId = $heading.text().replace(/\s+/g, "-").toLowerCase();
    $heading.attr("id", headingId);
    $heading.append(`<a class="anchorLink" href="#${headingId}">🔗</a>`);
    $(heading).hover(
      () => {
        $(heading)
          .find("a.anchorLink")
          .each((_, anchorLink) => {
            $(anchorLink).css("visibility", "visible");
          });
      },
      () => {
        $(heading)
          .find("a.anchorLink")
          .each((_, anchorLink) => {
            $(anchorLink).css("visibility", "hidden");
          });
      },
    );
  });

  if (result_html_div == null) return html_div.html();
}

function render_problem_text(md_id, html_id, placeholder = false) {
  const md_div = $(`#${md_id}`);
  const html_div = $(`#${html_id}`);

  // Replace occurrences of &gt; at the beginning of a new line with ">"
  // so Markdown blockquotes are handled correctly
  const md_text = md_div.html();
  render_markdown(md_text, html_div, placeholder);
}
