const swiperRoom = new Swiper(".section__related_swipper__room", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    1000: {
      slidesPerView: 2,
      spaceBetween: 30,
      grid: {
        fill: "row",
        rows: 1,
      },
    },
  },
});
