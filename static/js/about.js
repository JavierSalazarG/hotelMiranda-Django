const swiperAboutCounter = new Swiper(".swiper__counter_about", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination_about",
    clickable: true,
  },
  breakpoints: {
    1000: {
      slidesPerView: 2,
      spaceBetween: 30,
    },
  },
});
