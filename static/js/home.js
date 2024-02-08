const swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  cssMode: true,
  navigation: {
    prevEl: ".swiper-button-prev",
    nextEl: ".swiper-button-next",
  },
  breakpoints: {
    1000: {
      slidesPerView: 3,
    },
  },
  mousewheel: true,
  keyboard: true,
});

const swiperFacilities = new Swiper(".swiper-facilities", {
  slidesPerView: 1,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
  },
  breakpoints: {
    1000: {
      slidesPerView: 3,

      grid: {
        fill: "row",
        rows: 2,
      },
    },
  },
});

const swiperMenu = new Swiper(".swiperMenu", {
  slidesPerView: 1,
  spaceBetween: 16,

  navigation: {
    prevEl: ".swiper-button-prev",
    nextEl: ".swiper-button-next",
  },
  breakpoints: {
    1000: {
      slidesPerView: 2,

      grid: {
        fill: "row",
        rows: 3,
      },
    },
  },
});

const swiperMenuImg = new Swiper(".swiperMenuImg", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,

  pagination: {
    el: ".swiper-pagination",
  },
  breakpoints: {
    1000: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
  },
});
