-- 創建資料表來儲存匯入時間資訊
CREATE TABLE IF NOT EXISTS import_dates (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    import_date DATETIME NOT NULL,
    timezone_type INTEGER NOT NULL,
    timezone VARCHAR(50) NOT NULL
);
-- 創建主要的活動/展覽資訊表
CREATE TABLE IF NOT EXISTS events (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uid VARCHAR(100) NOT NULL,
    activity_name TEXT NOT NULL,
    description TEXT,
    organizer VARCHAR(200),
    address TEXT,
    start_date DATE,
    end_date DATE,
    location VARCHAR(200),
    latitude DECIMAL(12, 8),
    longitude DECIMAL(12, 8),
    ticket_price TEXT,
    related_link TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- 創建查詢結果資訊表
CREATE TABLE IF NOT EXISTS query_results (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    query_timestamp VARCHAR(50) NOT NULL,
    limit_count INTEGER NOT NULL,
    offset_count INTEGER NOT NULL,
    total_count INTEGER NOT NULL,
    sort_order VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- 創建關聯表，連接查詢結果和事件
CREATE TABLE IF NOT EXISTS query_event_relations (
    query_id BIGINT NOT NULL,
    event_id BIGINT NOT NULL,
    display_order INTEGER NOT NULL,
    PRIMARY KEY (query_id, event_id),
    FOREIGN KEY (query_id) REFERENCES query_results(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);
-- 創建娛樂資訊表（如果不存在）
CREATE TABLE IF NOT EXISTS entertainment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NULL,
    location VARCHAR(255) NULL,
    start_date DATE NULL,
    end_date DATE NULL,
    organizer VARCHAR(255) NULL,
    website VARCHAR(255) NULL,
    image_url VARCHAR(255) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    source VARCHAR(50) NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;