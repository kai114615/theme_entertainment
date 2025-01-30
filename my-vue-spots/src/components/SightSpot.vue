<template>
  <div class="sight-spot">
    <div class="hero-section">
      <h1>主題趣樂</h1>
      <p>精彩活動盡在眼前</p>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="搜尋活動...">
        <button><i class="fas fa-search"></i></button>
      </div>
    </div>

    <!-- 載入中提示 -->
    <div v-if="isLoading" class="loading-container">
      <div class="loading-spinner"></div>
      <p>正在載入活動資料...</p>
    </div>

    <!-- 錯誤提示 -->
    <div v-else-if="error" class="error-container">
      <p><i class="fas fa-exclamation-circle"></i> {{ error }}</p>
      <button @click="fetchAllEvents" class="retry-btn">重試</button>
    </div>

    <!-- 活動列表 -->
    <div v-else class="events-grid">
      <div v-for="event in filteredEvents" :key="event.uid" class="event-card" @click="openEventDetail(event)">
        <div class="event-image">
          <img :src="event.imageUrl" :alt="event.title" @error="handleImageError">
          <div class="event-date">
            <span>{{ formatDateShort(event.startDate) }}</span>
          </div>
        </div>
        <div class="event-info">
          <h3>{{ event.title }}</h3>
          <p class="event-time">
            <i class="fas fa-clock"></i>
            {{ formatTime(event.startDate) }} - {{ formatTime(event.endDate) }}
          </p>
          <p class="event-location" v-if="event.location">
            <i class="fas fa-map-marker-alt"></i>
            {{ event.location }}
          </p>
          <p class="event-organizer" v-if="event.organizer">
            <i class="fas fa-building"></i>
            {{ event.organizer }}
          </p>
        </div>
      </div>
    </div>

    <!-- 活動詳情彈窗 -->
    <div v-if="selectedEvent" class="modal" @click="selectedEvent = null">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="selectedEvent = null">&times;</button>
        <img :src="selectedEvent.imageUrl" :alt="selectedEvent.title" @error="handleImageError">
        <h2>{{ selectedEvent.title }}</h2>
        <div class="modal-info">
          <p v-if="selectedEvent.organizer">
            <i class="fas fa-building"></i> 主辦單位：{{ selectedEvent.organizer }}
          </p>
          <p>
            <i class="fas fa-calendar"></i> 活動時間：
            <br>
            <span class="time-info">{{ formatDate(selectedEvent.startDate) }} - {{ formatDate(selectedEvent.endDate)
              }}</span>
          </p>
          <p v-if="selectedEvent.location">
            <i class="fas fa-map-marker-alt"></i> 活動地點：{{ selectedEvent.location }}
          </p>
          <p class="description-title">活動介紹：</p>
          <p class="modal-description">{{ selectedEvent.description }}</p>
          <a v-if="selectedEvent.url" :href="selectedEvent.url" target="_blank" class="website-link">
            <i class="fas fa-external-link-alt"></i> 前往活動網站
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SightSpot',
  data() {
    return {
      searchQuery: '',
      events: [],
      isLoading: false,
      error: null,
      fallbackImage: 'https://via.placeholder.com/400x300?text=活動圖片',
      selectedEvent: null
    }
  },
  async created() {
    await this.fetchAllEvents();
  },
  computed: {
    filteredEvents() {
      return this.events.filter(event => {
        const matchesSearch =
          event.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          event.description.toLowerCase().includes(this.searchQuery.toLowerCase());
        return matchesSearch && event.imageUrl;
      });
    }
  },
  methods: {
    async fetchAllEvents() {
      this.isLoading = true;
      this.error = null;
      try {
        const response = await fetch('http://localhost:8000/api/events/', {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
          }
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // 確保所有日期格式正確
        this.events = data.map(event => ({
          ...event,
          startDate: event.startDate ? new Date(event.startDate).toISOString() : null,
          endDate: event.endDate ? new Date(event.endDate).toISOString() : null
        })).filter(event => event.imageUrl);

        console.log('獲取到的活動數據:', this.events);
      } catch (error) {
        console.error('獲取活動資料時發生錯誤:', error);
        this.error = '獲取活動資料時發生錯誤，請稍後再試';
      } finally {
        this.isLoading = false;
      }
    },

    openEventDetail(event) {
      this.selectedEvent = event;
    },

    handleImageError(e) {
      e.target.src = this.fallbackImage;
    },

    formatDate(dateStr) {
      if (!dateStr) return '';
      const date = new Date(dateStr);
      return date.toLocaleString('zh-TW', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      });
    },

    formatDateShort(dateStr) {
      if (!dateStr) return '';
      const date = new Date(dateStr);
      return date.toLocaleDateString('zh-TW', {
        month: 'long',
        day: 'numeric'
      });
    },

    formatTime(dateStr) {
      if (!dateStr) return '';
      const date = new Date(dateStr);
      return date.toLocaleTimeString('zh-TW', {
        hour: '2-digit',
        minute: '2-digit'
      });
    }
  }
}
</script>

<style scoped>
.sight-spot {
  padding: 20px;
  background-color: #f5f6fa;
  min-height: 100vh;
}

.hero-section {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url('https://images.unsplash.com/photo-1492684223066-81342ee5ff30');
  background-size: cover;
  background-position: center;
  color: white;
  margin: -20px -20px 20px -20px;
  border-radius: 0 0 20px 20px;
}

.hero-section h1 {
  font-size: 3em;
  margin-bottom: 10px;
  font-weight: bold;
}

.search-bar {
  max-width: 600px;
  margin: 20px auto;
  display: flex;
  gap: 10px;
}

.search-bar input {
  flex: 1;
  padding: 15px 25px;
  border: none;
  border-radius: 30px;
  font-size: 1.1em;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.search-bar button {
  padding: 15px 30px;
  border: none;
  border-radius: 30px;
  background: #3498db;
  color: white;
  cursor: pointer;
  transition: background 0.3s;
}

.search-bar button:hover {
  background: #2980b9;
}

.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 30px;
  padding: 100px;
}

.event-card {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 3px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.event-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.event-image {
  position: relative;
  height: 300px;
}

.event-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.event-date {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(52, 141, 219, 0.9);
  color: white;
  padding: 8px 15px;
  border-radius: 10px;
  font-size: 0.5em;
}

.event-info {
  padding: 20px;
}

.event-info h3 {
  margin: 0 0 15px 0;
  font-size: 1.5em;
  color: #2c3e50;
  line-height: 1.5;
}

.event-time,
.event-location,
.event-organizer {
  color: #666;
  margin: 8px 0;
  font-size: 1.0em;
  display: flex;
  align-items: center;
  gap: 10px;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 20px;
  max-width: 800px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.close-btn {
  position: absolute;
  right: 20px;
  top: 20px;
  background: rgba(0, 0, 0, 0.1);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s;
}

.close-btn:hover {
  background: rgba(0, 0, 0, 0.2);
}

.modal-content img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  border-radius: 15px;
  margin-bottom: 20px;
}

.modal-info {
  color: #2c3e50;
}

.modal-info p {
  margin: 15px 0;
  line-height: 1.6;
}

.modal-description {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  margin: 15px 0;
  line-height: 1.8;
}

.website-link {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 25px;
  background: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 25px;
  transition: background 0.3s;
}

.website-link:hover {
  background: #2980b9;
}

.loading-container,
.error-container {
  text-align: center;
  padding: 50px;
  margin: 20px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 3px 15px rgba(0, 0, 0, 0.1);
}

.loading-spinner {
  width: 50px;
  height: 50px;
  margin: 0 auto 20px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.retry-btn {
  margin-top: 20px;
  padding: 12px 25px;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: background 0.3s;
}

.retry-btn:hover {
  background: #c0392b;
}

@media (max-width: 768px) {
  .hero-section {
    padding: 40px 20px;
  }

  .events-grid {
    grid-template-columns: 1fr;
    padding: 10px;
  }

  .modal-content {
    padding: 20px;
    width: 95%;
  }

  .modal-content img {
    height: 300px;
  }
}
</style>