<template>
    <div class="banner">
        <div class="banner-container">
            <div class="logo-section">
                <div class="logo">
                    <i class="fa-solid fa-mountain-sun" style="color: #FFD43B;"></i>
                </div>
                <span class="logo-text">主題趣樂</span>
            </div>
            <nav class="nav-section">
                <a href="#" class="nav-link active">首頁</a>
                <a href="http://localhost:8000/create.html" class="nav-link">最新活動</a>
                <a href="http://localhost:8000/activity_management.html" class="nav-link">網站導覽</a>
                <a href="http://localhost:8000/list.html" class="nav-link">聯絡我們</a>
                <a href="#" class="nav-link login-btn">
                    <i class="fas fa-user"></i> 登入會員
                </a>
            </nav>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Banner'
}
</script>

<style scoped>
.banner {
    background-color: #4A90E2;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.banner-container {
    max-width: 1500px;
    margin: auto;
    padding: 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    /* padding-right: 10rem; */
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 1rem;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.logo-section:hover {
    transform: scale(1.05);
}

.logo {
    font-size: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    /* background: linear-gradient(135deg, #fff8e6 0%, #fff5d6 100%); */
    border-radius: 12px;
}

.logo-text {
    font-size: 1.5rem;
    font-weight: bold;
    color: #FFFFFF;
}

.nav-section {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    margin-left: 10%;
}

.nav-link {
    text-decoration: none;
    color: #FFFFFF;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.nav-link:hover {
    color: #4A90E2;
    background-color: #FFFFFF;
}

.nav-link.active {
    color: #4A90E2;
    background-color: #FFFFFF;
}

.login-btn {
    background-color: #3498db;
    color: white !important;
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    box-shadow: 0 2px 10px rgba(52, 152, 219, 0.2);
}

.login-btn:hover {
    background-color: #2980b9;
    color: white !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
}

@media (max-width: 768px) {
    .banner-container {
        flex-direction: column;
        padding: 1rem;
        gap: 1rem;
    }

    .nav-section {
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
    }

    .nav-link {
        padding: 0.5rem;
        font-size: 0.9rem;
    }

    .logo {
        font-size: 2rem;
        width: 40px;
        height: 40px;
    }

    .logo-text {
        font-size: 1.3rem;
    }
}
</style>
