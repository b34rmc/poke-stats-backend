const data = {
  1: {
    id: 1,
    name: "Bulbasaur",
    stats: {
      base_stamina: "90",
      base_defense: "118",
      base_attack: "118",
      name: "Bulbasaur",
      id: 1,
    },
    type: ["grass", "poison"],
    boosted_weather: ["sunny", "cloudy"],
    charged_moves: ["sludge bomb", "seed bomb", "power whip"],
    elite_charged_moves: [],
    elite_fast_moves: [],
    fast_moves: ["vine whip", "tackle"],
    max_cp: 981,
    official_front_default:
      "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
    official_front_shiny:
      "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/1.png",
  },
  2: {
    id: 2,
    name: "Ivysaur",
  },
  3: {
    id: 3,
    name: "Venusaur",
  },
};

// 10800 seconds = 3 hours. spread every request 8.29 seconds apart
