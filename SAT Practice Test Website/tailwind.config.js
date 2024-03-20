/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "marian-blue": "#424874",         /** color palette 1 */
        "light-periwinkle": "#dcd6f7",
        "mid-periwinkle": "#a6b1e1",
        "french-gray": "#cacfd6",
        "azure-web": "#d6e5e3"
      }
    },
  },
  plugins: [],
}

