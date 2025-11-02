# 🌱 PlantPal - Your Virtual Garden Sanctuary

A beautiful, interactive virtual garden management system built with Django and vanilla JavaScript. Grow plants, track their health, earn coins, and compete on leaderboards!

![PlantPal Banner](https://via.placeholder.com/800x200/d1fae5/059669?text=PlantPal+-+Your+Garden+Awaits)

## ✨ Features

### 🌿 Core Features
- **Virtual Garden**: Plant and grow a variety of plants (herbs, flowers, cacti, exotic plants)
- **Plant Care**: Water plants to maintain health and earn coins
- **Growth System**: Plants grow realistically over 4 days through stages (Seed → Sprout → Growing → Mature)
- **Health Tracking**: Monitor plant health with visual progress bars

### 🎨 Customization
- **Plant Personalization**: Rename plants, add custom emojis (16 options), and write plant bios
- **Theme Toggle**: Switch between beautiful day and night modes
- **Weather Effects**: Add rain ☔, snow ❄️, or clear ☀️ weather to your garden

### 🏆 Gamification
- **Coin System**: Earn 5 coins per watering
- **Streak Tracking**: Build daily login streaks
- **Leaderboards**: Compete in 4 categories:
  - 🔥 Weekly Streaks
  - 🌈 Garden Diversity
  - 💰 Total Coins
  - 🌱 Most Plants

### 🛒 Shop System
- **6+ Plant Varieties**: Common to Legendary rarities
- **Special Events**: Rare plants appear during special conditions (e.g., Moonflower during full moon)
- **Rarity Tiers**: Common, Uncommon, Rare, Legendary, Mythic

### 📊 Advanced Features
- **Activity History**: Track all your gardening actions
- **Persistent Storage**: Data saves automatically across sessions
- **Watering History**: Complete log of all plant care activities
- **Growth Analytics**: Monitor plant growth over time

---

## 🖼️ Screenshots

### Garden View
![Garden View](https://via.placeholder.com/600x400/a7f3d0/059669?text=Garden+View)

### Dashboard
![Dashboard](https://via.placeholder.com/600x400/fef3c7/92400e?text=Dashboard)

### Shop
![Shop](https://via.placeholder.com/600x400/f3e8ff/9333ea?text=Plant+Shop)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/sanskaaar01/plantpal.git
   cd plantpal
```

2. **Create virtual environment**
```bash
   python -m venv venv
```

3. **Activate virtual environment**
   - Windows:
```bash
     venv\Scripts\activate
```
   - Mac/Linux:
```bash
     source venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install -r requirements.txt
```

5. **Run migrations**
```bash
   python manage.py migrate
```

6. **Start the development server**
```bash
   python manage.py runserver
```

7. **Open your browser**
```
   http://localhost:8000/
```

---

## 📦 Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Storage**: Browser localStorage API (frontend) / SQLite (backend ready)
- **Animation**: CSS keyframes
- **Icons**: SVG graphics

---

## 🎮 How to Play

1. **Login**: Enter a username to start your garden
2. **Visit Shop**: Purchase your first plant with starting coins (50)
3. **Water Plants**: Click the water button to keep plants healthy (+5 coins per water)
4. **Watch Growth**: Plants grow automatically over 4 days
5. **Customize**: Click plants to rename, add emojis, and write bios
6. **Compete**: Check leaderboards to see how you rank
7. **Daily Streaks**: Login daily to build your streak multiplier

---

## 🌟 Plant Varieties

| Plant | Type | Rarity | Cost | Emoji |
|-------|------|--------|------|-------|
| Lavender | Aromatic | Common | 50 | 🌿 |
| Cactus | Desert | Common | 45 | 🌵 |
| Sunflower | Flowering | Common | 60 | 🌻 |
| Rose | Flowering | Uncommon | 75 | 🌹 |
| Orchid | Exotic | Uncommon | 85 | 🌸 |
| Bamboo | Exotic | Uncommon | 95 | 🎋 |
| Bonsai | Miniature | Rare | 120 | 🎋 |
| Venus Flytrap | Carnivorous | Legendary | 200 | 🪴 |
| Moonflower* | Mystical | Mythic | 300 | 🌙 |

*Special event plant - available only during full moon nights

---

## 🎨 Customization Options

### Plant Emojis
🌱 🌿 🍀 🌵 🌴 🌳 🌲 🎋 🎍 🌾 🌺 🌻 🌷 🌹 🥀 🌸

### Weather Effects
- ☀️ Clear skies
- 🌧️ Gentle rain
- ❄️ Snowfall

### Themes
- 🌞 Day Mode: Bright, vibrant colors
- 🌙 Night Mode: Cool, calming tones

---

## 📂 Project Structure
```
plantpal_project/
├── garden/                      # Main Django app
│   ├── templates/
│   │   └── garden/
│   │       └── index.html      # Main application
│   ├── static/                 # Static files (future)
│   ├── views.py               # Django views
│   ├── urls.py                # URL routing
│   └── models.py              # Database models (future)
├── plantpal_project/          # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/                      # Virtual environment
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

---

## 🔮 Future Features (Roadmap)

- [ ] Database integration for persistent storage
- [ ] User authentication system
- [ ] Multiplayer features (visit friends' gardens)
- [ ] Plant breeding system
- [ ] Seasonal events and challenges
- [ ] Mobile app (React Native)
- [ ] Plant encyclopedia with care tips
- [ ] Achievement badges system
- [ ] Garden themes and backgrounds
- [ ] Sound effects and music
- [ ] Plant trading marketplace
- [ ] Weather forecast affects plant growth
- [ ] Pest control mini-games

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Bug description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@sanskaaar01](https://github.com/sanskaaar01)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Inspired by virtual pet games and farming simulators
- Built with ❤️ using Django
- Plant emojis from Unicode Consortium
- Community feedback and suggestions


---

## 🎯 Development Status

- [x] Core functionality
- [x] Plant growth system
- [x] Shop system
- [x] Leaderboards
- [x] History tracking
- [x] Customization
- [ ] Backend integration
- [ ] User authentication
- [ ] Mobile responsive optimization
- [ ] PWA support

---

## 💡 Tips & Tricks

1. **Water regularly**: Set reminders to water plants daily for maximum health
2. **Save coins**: Wait for special events to get rare plants
3. **Build streaks**: Login daily to climb the leaderboard
4. **Diversify**: Collect different plant types for diversity bonus
5. **Customize early**: Give your plants personality from the start

---

## 🌐 Live Demo

[🔗 Try PlantPal Live](https://your-demo-url.com) *(Coming soon)*

---

## 📞 Support

Need help? Reach out:
- 📧 Email: bhoslesanskar@gmail.com


---

<div align="center">

**Made with 🌱 and 💚 by passionate gardeners**

⭐ Star this repo if you love PlantPal!

</div>