const swiperPopular = new Swiper(".section__popular_swiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    1000: {
      slidesPerView: 3,
      spaceBetween: 30,
      grid: {
        fill: "row",
        rows: 1,
      },
    },
  },
});
