const input = document.getElementById("movieInput");
const button = document.getElementById("searchBtn");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  const title = input.value.trim();

  if (!title) {
    result.innerHTML = "<p>请输入电影或电视剧名称。</p>";
    return;
  }

  result.innerHTML = "<p>正在搜索...</p>";

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/search?title=${encodeURIComponent(title)}`
    );

    const data = await response.json();

    if (data.error) {
      result.innerHTML = "<p>没有找到相关结果。</p>";
      return;
    }

    const typeMap = {
      flatrate: "订阅观看",
      rent: "租赁观看",
      buy: "购买观看"
    };

    const providerList = data.providers
      .map(provider => {
        return `
          <div class="provider-card">
            ${provider.logo ? `<img class="provider-logo" src="${provider.logo}">` : ""}
            <div>
              <strong>${provider.name}</strong>
              <p>${typeMap[provider.type] || provider.type}</p>
            </div>
          </div>
        `;
      })
      .join("");

    result.innerHTML = `
      <h3>${data.title} (${data.year})</h3>

      ${data.poster ? `<img class="poster" src="${data.poster}">` : ""}

      <p>${data.overview || "暂无简介。"}</p>

      ${
        data.watch_link
          ? `<a class="watch-btn" href="${data.watch_link}" target="_blank">
              查看合法观看入口
            </a>`
          : ""
      }

      <h4>可观看平台</h4>

      <div class="provider-list">
        ${providerList || "<p>暂未找到可观看平台。</p>"}
      </div>
    `;
  } catch (error) {
    result.innerHTML = "<p>后端连接失败，请确认 FastAPI 正在运行。</p>";
  }
});