<template>
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>關於主題趣樂</h3>
                <p>我們致力於為您提供最新、最精彩的活動資訊，讓您的生活更加豐富多彩。無論是藝術展覽、音樂會、戶外活動還是美食節慶，這裡都能找到適合您的活動。</p>
            </div>
            <div class="footer-section">
                <h3>快速連結</h3>
                <ul>
                    <li><a href="#">首頁</a></li>
                    <li><a href="#">熱門活動</a></li>
                    <li><a href="#">最新消息</a></li>
                    <li><a href="#">活動分類</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>追蹤我們</h3>
                <div class="social-links">
                    <a href="#" class="social-link"><i class="fab fa-facebook"></i></a>
                    <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
                    <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="social-link"><i class="fab fa-youtube"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 主題趣樂 | 版權所有</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped>
.footer {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 4rem 0 0;
    margin-top: 3rem;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
}

.footer-section h3 {
    color: #3498db;
    margin-bottom: 1.5rem;
    font-size: 1.3rem;
}

.footer-section p {
    line-height: 1.6;
    color: #bdc3c7;
}

.footer-section ul {
    list-style: none;
    padding: 0;
}

.footer-section ul li {
    margin-bottom: 0.8rem;
}

.footer-section ul li a {
    color: #bdc3c7;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-section ul li a:hover {
    color: #3498db;
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background-color: #34495e;
    color: #ecf0f1;
    border-radius: 50%;
    text-decoration: none;
    transition: all 0.3s ease;
}

.social-link:hover {
    background-color: #3498db;
    transform: translateY(-3px);
}

.footer-bottom {
    margin-top: 3rem;
    padding: 1.5rem;
    text-align: center;
    background-color: #1a252f;
}

.footer-bottom p {
    margin: 0;
    color: #bdc3c7;
}

@media (max-width: 768px) {
    .footer {
        padding: 2rem 0 0;
    }

    .footer-content {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 2rem;
    }

    .social-links {
        justify-content: center;
    }
}
</style>