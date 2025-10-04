// Game data - will be loaded from JSON file
let gamesData = [];

// DOM elements - will be initialized after DOM loads
let hamburger, navMenu, navLinks, searchInput, searchBtn, gamesGrid, loadMoreBtn, categoryTags;
let gameModal, modalGameTitle, gameFrame, closeModal, fullscreenBtn, refreshBtn;

// Global variables
let currentGames = gamesData;
let displayedGames = 6;
let currentFilter = 'all';

// Hero section slideshow variables
let currentSlideIndex = 0;
let slideInterval;

// Asynchronously load game data
async function loadGamesData() {
    console.log('Starting to load game data...');
    try {
        const response = await fetch('data/games.json?' + Date.now());
        console.log('Network request response status:', response.status);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        gamesData = data;
        console.log('Game data loaded successfully:', gamesData.length, 'games');
        console.log('First 5 games:', gamesData.slice(0, 5).map(g => g.title));
        return data;
    } catch (error) {
        console.error('Error loading game data:', error);
        // If loading fails, use fallback data
        gamesData = getFallbackGamesData();
        console.log('Using fallback data:', gamesData.length, 'games');
        return gamesData;
    }
}

// Fallback game data (used when JSON loading fails)
function getFallbackGamesData() {
    return [
        {
            id: 1,
            title: "Space Adventure",
            image_url: "https://via.placeholder.com/300x200/667eea/ffffff?text=Space+Adventure",
            description: "Embark on an epic adventure journey in the vast universe, explore unknown planets, and battle alien creatures.",
            category: "action",
            tags: ["sci-fi", "adventure", "single-player"]
        },
        {
            id: 2,
            title: "Sudoku Master",
            image_url: "https://via.placeholder.com/300x200/764ba2/ffffff?text=Sudoku+Master",
            description: "Challenge classic Sudoku puzzles, from easy to difficult, improve your logical thinking skills.",
            category: "puzzle",
            tags: ["puzzle", "logic", "single-player"]
        }
    ];
}

// Initialize DOM elements
function initializeDOMElements() {
    hamburger = document.querySelector('.hamburger');
    navMenu = document.querySelector('.nav-menu');
    navLinks = document.querySelectorAll('.nav-link');
    searchInput = document.querySelector('#searchInput');
    searchBtn = document.querySelector('.search-btn');
    gamesGrid = document.querySelector('#gamesGrid');
    loadMoreBtn = document.querySelector('#loadMoreBtn');
    categoryTags = document.querySelectorAll('.category-tag');
    
    // Modal elements
    gameModal = document.querySelector('#gameModal');
    modalGameTitle = document.querySelector('#modalGameTitle');
    gameFrame = document.querySelector('#gameFrame');
    closeModal = document.querySelector('#closeModal');
    fullscreenBtn = document.querySelector('#fullscreenBtn');
    refreshBtn = document.querySelector('#refreshBtn');
}

// 初始化
document.addEventListener('DOMContentLoaded', async function() {
    console.log('DOM 加載完成，開始初始化...');
    
    try {
        // 初始化 DOM 元素
        initializeDOMElements();
        console.log('DOM 元素初始化完成');
        
        // 顯示加載動畫
        showLoadingAnimation();
        console.log('顯示加載動畫');
        
        // 加載遊戲數據
        await loadGamesData();
        console.log('遊戲數據加載完成，數據量:', gamesData.length);
        
        // 更新 currentGames
        currentGames = gamesData;
        console.log('currentGames 更新完成，數據量:', currentGames.length);
        console.log('currentGames 前5個遊戲:', currentGames.slice(0, 5).map(g => g.title));
        
        // 初始化各個功能
        initializeNavigation();
        console.log('導航功能初始化完成');
        
        initializeSearch();
        console.log('搜索功能初始化完成');
        
        initializeGames();
        console.log('遊戲功能初始化完成');
        
        initializeCategories();
        console.log('類別功能初始化完成');
        
        initializeScrollEffects();
        console.log('滾動效果初始化完成');
        
        initializeAnimations();
        console.log('動畫效果初始化完成');
        
        initializeGameModal();
        console.log('遊戲模態框初始化完成');
        
        initializeHeroSlider();
        console.log('英雄區塊幻燈片初始化完成');
        
        // 隱藏加載動畫
        hideLoadingAnimation();
        console.log('隱藏加載動畫');
        
        console.log('所有初始化完成！');
        
    } catch (error) {
        console.error('初始化過程中發生錯誤:', error);
        // 即使出錯也要隱藏加載動畫
        hideLoadingAnimation();
    }
});

// 導航功能
function initializeNavigation() {
    // 手機版選單切換
    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // 導航連結點擊
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // 如果是外部链接（不以#开头），允许默认行为
            if (!href.startsWith('#')) {
                // 移除所有 active 類
                navLinks.forEach(l => l.classList.remove('active'));
                // 添加 active 類到當前連結
                this.classList.add('active');
                
                // 關閉手機版選單
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                
                // 允许外部链接正常跳转
                return true;
            }
            
            // 对于内部锚点链接，阻止默认行为并处理
            e.preventDefault();
            
            // 移除所有 active 類
            navLinks.forEach(l => l.classList.remove('active'));
            // 添加 active 類到當前連結
            this.classList.add('active');
            
            // 關閉手機版選單
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            
            // 檢查是否有類別篩選
            const category = this.getAttribute('data-category');
            if (category) {
                // 篩選遊戲
                filterGamesByCategory(category);
            } else {
                // 平滑滾動到對應區塊
                const targetId = this.getAttribute('href');
                if (targetId.startsWith('#')) {
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            }
        });
    });

    // 滾動時更新導航狀態
    window.addEventListener('scroll', updateNavigationOnScroll);
}

// 搜尋功能（導航欄）
function initializeSearch() {
    if (searchBtn && searchInput) {
        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
        
        // 即時搜尋
        searchInput.addEventListener('input', function() {
            if (this.value.length > 2) {
                performSearch();
            } else if (this.value.length === 0) {
                resetGames();
            }
        });
    }
}

// 舊的搜索功能（導航欄）
function performSearch() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    
    if (searchTerm === '') {
        resetGames();
        return;
    }
    
    currentGames = gamesData.filter(game => 
        game.title.toLowerCase().includes(searchTerm) ||
        game.description.toLowerCase().includes(searchTerm) ||
        game.category.toLowerCase().includes(searchTerm) ||
        (game.tags && game.tags.some(tag => tag.toLowerCase().includes(searchTerm)))
    );
    
    displayGames(currentGames);
    showSearchResults(searchTerm);
}

function resetGames() {
    currentGames = gamesData;
    currentFilter = 'all';
    displayedGames = 6;
    displayGames(currentGames);
    hideSearchResults();
}

function showSearchResults(searchTerm) {
    const resultsText = document.createElement('div');
    resultsText.className = 'search-results';
    resultsText.innerHTML = `
        <p>搜尋 "${searchTerm}" 的結果：找到 ${currentGames.length} 個遊戲</p>
    `;
    
    // 移除舊的搜尋結果
    const oldResults = document.querySelector('.search-results');
    if (oldResults) {
        oldResults.remove();
    }
    
    // 添加新的搜尋結果
    gamesGrid.parentNode.insertBefore(resultsText, gamesGrid);
}

function hideSearchResults() {
    const resultsText = document.querySelector('.search-results');
    if (resultsText) {
        resultsText.remove();
    }
}

// 遊戲顯示功能
function initializeGames() {
    console.log('初始化遊戲功能...');
    console.log('gamesGrid:', gamesGrid);
    console.log('currentGames:', currentGames);
    console.log('gamesData:', gamesData);
    
    if (!gamesGrid) {
        console.error('找不到 gamesGrid 元素！');
        return;
    }
    
    if (!currentGames || currentGames.length === 0) {
        console.error('沒有遊戲數據！');
        return;
    }
    
    displayGames(currentGames);
    
    // 載入更多按鈕
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            displayedGames += 6;
            displayGames(currentGames);
            
            // 如果已顯示所有遊戲，隱藏按鈕
            if (displayedGames >= currentGames.length) {
                this.style.display = 'none';
            }
        });
    }
}

function displayGames(games) {
    console.log('displayGames 被調用，遊戲數量:', games.length);
    
    if (!gamesGrid) {
        console.error('gamesGrid 不存在！');
        return;
    }
    
    gamesGrid.innerHTML = '';
    
    const gamesToShow = games.slice(0, displayedGames);
    console.log('要顯示的遊戲數量:', gamesToShow.length);
    
    gamesToShow.forEach((game, index) => {
        const gameCard = createGameCard(game);
        gameCard.style.animationDelay = `${index * 0.1}s`;
        gameCard.classList.add('fade-in-up');
        gamesGrid.appendChild(gameCard);
    });
    
    // 更新載入更多按鈕
    if (loadMoreBtn) {
        if (displayedGames >= games.length) {
            loadMoreBtn.style.display = 'none';
        } else {
            loadMoreBtn.style.display = 'block';
        }
    }
}

function createGameCard(game) {
    const card = document.createElement('div');
    card.className = 'game-card';
    card.setAttribute('data-category', game.category);
    
    // 生成標籤 HTML
    const tagsHtml = game.tags ? game.tags.map(tag => `<span class="game-tag">${tag}</span>`).join('') : '';
    
    card.innerHTML = `
        <div class="game-image">
            <img src="${game.image_url}" alt="${game.title} - ${game.category} game, tags: ${game.tags ? game.tags.join(', ') : 'none'}" loading="lazy" onerror="handleImageError(this);">
            <div class="game-image-fallback" style="display: none;">
                <i class="fas fa-gamepad"></i>
                <span>${game.title}</span>
            </div>
        </div>
        <div class="game-info">
            <h3 class="game-title">${game.title}</h3>
            <p class="game-description">${game.description}</p>
            <div class="game-tags">
                ${tagsHtml}
            </div>
            <div class="game-meta">
                <div class="game-category">
                    <i class="fas fa-tag"></i>
                    <span>${game.category}</span>
                </div>
            </div>
            <button class="play-btn" onclick="openGameModal(${game.id})">
                <i class="fas fa-play"></i> Start Game
            </button>
        </div>
    `;
    
    return card;
}

// 遊戲類別功能
function initializeCategories() {
    // 由於我們刪除了分類篩選區域，這個函數現在主要處理導航欄中的分類鏈接
    // 分類功能已經在 initializeNavigation() 中處理
    console.log('分類功能已整合到導航功能中');
}

function filterGamesByCategory(category) {
    currentFilter = category;
    
    if (category === 'all') {
        currentGames = gamesData;
    } else {
        // 將英文類別映射到中文類別
        const categoryMap = {
            'action': '動作遊戲',
            'puzzle': '解謎遊戲', 
            'racing': '競速遊戲',
            'sports': '運動遊戲',
            'shooting': '射擊遊戲',
            'simulator': '模擬遊戲'
        };
        
        const targetCategory = categoryMap[category] || category;
        currentGames = gamesData.filter(game => game.category === targetCategory);
    }
    
    displayedGames = 6;
    displayGames(currentGames);
    
    // 滾動到遊戲區塊
    document.querySelector('.featured-games').scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

// 遊戲模態框功能
function initializeGameModal() {
    // 關閉按鈕
    closeModal.addEventListener('click', closeGameModal);
    
    // 全螢幕按鈕
    fullscreenBtn.addEventListener('click', toggleFullscreen);
    
    // 重新載入按鈕
    refreshBtn.addEventListener('click', refreshGame);
    
    // 點擊模態框背景關閉
    gameModal.addEventListener('click', function(e) {
        if (e.target === gameModal) {
            closeGameModal();
        }
    });
    
    // ESC 鍵關閉
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && gameModal.classList.contains('active')) {
            closeGameModal();
        }
    });
}

function openGameModal(gameId) {
    const game = gamesData.find(g => g.id === gameId);
    if (!game) {
        console.error('找不到遊戲:', gameId);
        return;
    }
    
    // 設置模態框標題
    modalGameTitle.textContent = game.title;
    
    // 設置 iframe 源
    if (game.game_link) {
        gameFrame.src = game.game_link;
    } else {
        // 如果沒有遊戲連結，顯示提示
        gameFrame.src = 'about:blank';
        gameFrame.style.display = 'none';
        const placeholder = document.createElement('div');
        placeholder.style.cssText = `
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            background: #f8f9fa;
            color: #666;
            font-size: 1.2rem;
        `;
        placeholder.innerHTML = `
            <i class="fas fa-gamepad" style="font-size: 3rem; margin-bottom: 1rem; color: #667eea;"></i>
            <p>遊戲載入中...</p>
            <p style="font-size: 0.9rem; margin-top: 0.5rem;">如果遊戲無法載入，請檢查網路連接</p>
        `;
        gameFrame.parentNode.appendChild(placeholder);
    }
    
    // 顯示模態框
    gameModal.classList.add('active');
    document.body.style.overflow = 'hidden'; // 防止背景滾動
    
    console.log('打開遊戲模態框:', game.title);
}

function closeGameModal() {
    gameModal.classList.remove('active');
    gameModal.classList.remove('fullscreen');
    document.body.style.overflow = ''; // 恢復滾動
    
    // 清除 iframe 源
    gameFrame.src = 'about:blank';
    
    // 移除佔位符
    const placeholder = gameFrame.parentNode.querySelector('div');
    if (placeholder && placeholder !== gameFrame) {
        placeholder.remove();
    }
    gameFrame.style.display = 'block';
    
    console.log('關閉遊戲模態框');
}

function toggleFullscreen() {
    gameModal.classList.toggle('fullscreen');
    const isFullscreen = gameModal.classList.contains('fullscreen');
    
    if (isFullscreen) {
        fullscreenBtn.innerHTML = '<i class="fas fa-compress"></i> 退出全螢幕';
    } else {
        fullscreenBtn.innerHTML = '<i class="fas fa-expand"></i> 全螢幕';
    }
    
    console.log('切換全螢幕模式:', isFullscreen);
}

function refreshGame() {
    if (gameFrame.src && gameFrame.src !== 'about:blank') {
        gameFrame.src = gameFrame.src;
        console.log('重新載入遊戲');
    }
}

// 滾動效果
function initializeScrollEffects() {
    // 滾動時更新導航狀態
    window.addEventListener('scroll', updateNavigationOnScroll);
}

function updateNavigationOnScroll() {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
}

// 動畫效果
function initializeAnimations() {
    // 添加淡入動畫
    const style = document.createElement('style');
    style.textContent = `
        .fade-in-up {
            animation: fadeInUp 0.6s ease-out forwards;
            opacity: 0;
            transform: translateY(30px);
        }
        
        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);
}

// 加載動畫
function showLoadingAnimation() {
    const loadingOverlay = document.createElement('div');
    loadingOverlay.id = 'page-loading-overlay';
    loadingOverlay.innerHTML = `
        <div class="loading-content">
            <div class="loading-spinner"></div>
            <h3>Loading Games...</h3>
            <p>Please wait, exciting games are loading</p>
        </div>
    `;
    
    document.body.appendChild(loadingOverlay);
    
    // 添加樣式
    const style = document.createElement('style');
    style.textContent = `
        #page-loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            color: white;
            pointer-events: none;
            opacity: 0.8;
        }
        .loading-content {
            text-align: center;
        }
        .loading-spinner {
            width: 60px;
            height: 60px;
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-top: 4px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(style);
}

function hideLoadingAnimation() {
    const loadingOverlay = document.getElementById('page-loading-overlay');
    if (loadingOverlay) {
        loadingOverlay.style.opacity = '0';
        loadingOverlay.style.transition = 'opacity 0.5s ease';
        setTimeout(() => {
            loadingOverlay.remove();
        }, 500);
    }
}

// 英雄區塊幻燈片功能
function initializeHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    
    console.log('初始化幻灯片，找到', slides.length, '个幻灯片');
    
    if (slides.length === 0) {
        console.error('没有找到幻灯片元素');
        return;
    }
    
    // 确保只有第一个幻灯片是active状态
    slides.forEach((slide, index) => {
        if (index === 0) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
    
    // 确保只有第一个指示点是active状态
    dots.forEach((dot, index) => {
        if (index === 0) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
    
    // 重置当前幻灯片索引
    currentSlideIndex = 0;
    
    // 自動播放
    startAutoSlide();
    
    // 鼠標懸停時暫停自動播放
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        heroSection.addEventListener('mouseenter', stopAutoSlide);
        heroSection.addEventListener('mouseleave', startAutoSlide);
    }
    
    console.log('幻灯片初始化完成');
}

function startAutoSlide() {
    stopAutoSlide(); // 清除現有的定時器
    slideInterval = setInterval(() => {
        changeSlide(1);
    }, 5000); // 每5秒切換一次
}

function stopAutoSlide() {
    if (slideInterval) {
        clearInterval(slideInterval);
        slideInterval = null;
    }
}

// 全局函数，确保可以从HTML onclick调用
window.changeSlide = function(direction) {
    console.log('changeSlide 被调用，方向:', direction);
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    
    if (slides.length === 0) {
        console.error('没有找到幻灯片元素');
        return;
    }
    
    // 移除當前幻燈片的active類
    slides[currentSlideIndex].classList.remove('active');
    dots[currentSlideIndex].classList.remove('active');
    
    // 計算下一個幻燈片索引
    currentSlideIndex += direction;
    
    // 循環處理
    if (currentSlideIndex >= slides.length) {
        currentSlideIndex = 0;
    } else if (currentSlideIndex < 0) {
        currentSlideIndex = slides.length - 1;
    }
    
    // 添加active類到新的幻燈片
    slides[currentSlideIndex].classList.add('active');
    dots[currentSlideIndex].classList.add('active');
    
    console.log('幻灯片切换到索引:', currentSlideIndex);
}


// 全局函数，确保可以从HTML onclick调用
window.currentSlide = function(slideNumber) {
    console.log('currentSlide 被调用，幻灯片编号:', slideNumber);
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.dot');
    
    if (slides.length === 0) {
        console.error('没有找到幻灯片元素');
        return;
    }
    
    // 移除所有active類
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    // 設置新的索引
    currentSlideIndex = slideNumber - 1;
    
    // 添加active類
    slides[currentSlideIndex].classList.add('active');
    dots[currentSlideIndex].classList.add('active');
    
    console.log('幻灯片切换到索引:', currentSlideIndex);
    
    // 重新開始自動播放
    startAutoSlide();
}

// 圖片載入錯誤處理
function handleImageError(img) {
    console.log('圖片載入失敗:', img.src);
    img.style.display = 'none';
    const fallback = img.nextElementSibling;
    if (fallback) {
        fallback.style.display = 'flex';
    }
}