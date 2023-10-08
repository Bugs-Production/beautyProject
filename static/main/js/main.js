// Скрипт для шапки
$(document).ready(function() {
    var header = $(".sticky-header");
    var content = $(".content");
    var headerHeight = header.outerHeight();

    $(window).scroll(function() {
        if ($(this).scrollTop() > headerHeight) {
            header.addClass("sticky");
            content.css("margin-top", headerHeight);
        } else {
            header.removeClass("sticky");
            content.css("margin-top", 0);
        }
    });
});

// скрипт для сокращения текста в отзывах
$(document).ready(function() {
    // 250 characters are shown by default
    var showChar = 150;
    var dots = ".... ";
    var moreText = "eще";
    var lessText = "Скрыть";

    $('.show-text').each(function() {
        var content = $(this).html();

        if(content.length > showChar) {

            var cont = content.substr(0, showChar);
            var restOfTheText = content.substr(showChar, content.length - showChar);

            var html = cont + '<span class="dots">' + dots + '</span><span class="morecontent"><span>' + restOfTheText + '</span><a href="" class="morelink">' + moreText + '</a></span>';

            $(this).html(html);
        }

    });
    $(".morelink").click(function() {
        if($(this).hasClass("test")) {
            $(this).removeClass("test");
            $(this).html(moreText);
        } else {
            $(this).addClass("test");
            $(this).html(lessText);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
});

// скрипт для услуг
$(document).ready(function() {
  // Получаем все ссылки и блоки с ценами услуг
  var serviceLinks = $('.service-link');
  var serviceBlocks = $('.row.services-price');

  // Добавляем класс "active-link-services" к первой ссылке
  serviceLinks.first().addClass('active-link-services');

  // Добавляем обработчик клика на каждую ссылку
  serviceLinks.click(function(event) {
    event.preventDefault(); // Предотвращаем переход по ссылке
    var targetId = $(this).data('target');

    // Удаляем класс "active" у всех блоков
    serviceBlocks.removeClass('service-active');

    // Удаляем класс "active-link-services" у всех ссылок
    serviceLinks.removeClass('active-link-services');

    // Добавляем класс "active" к выбранному блоку
    $('#' + targetId).addClass('service-active');

    // Добавляем класс "active-link-services" к активной ссылке
    $(this).addClass('active-link-services');
  });
});

// скрипт для записи на маникюр
document.addEventListener("DOMContentLoaded", function() {
    // Находим все кнопки выбора маникюра
    const serviceButtons = document.querySelectorAll('[data-manicure-id]');

    // Находим все элементы с видами маникюра
    const manicureTypes = document.querySelectorAll('.manicure-type');

    // Добавляем обработчики событий для кнопок выбора маникюра
    serviceButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const manicureId = button.getAttribute('data-manicure-id');

            // Определяем вид маникюра, соответствующий выбранной кнопке
            const selectedManicure = document.getElementById('manicure_type_' + manicureId);

            // Проверяем текущее состояние видов маникюра и скрываем их, если они уже отображены
            manicureTypes.forEach(function(manicureType) {
                if (manicureType.style.display === 'block' && manicureType !== selectedManicure) {
                    manicureType.style.display = 'none';
                }
            });

            // Переключаем состояние видимости выбранного вида маникюра
            if (selectedManicure) {
                if (selectedManicure.style.display === 'block') {
                    selectedManicure.style.display = 'none';
                } else {
                    selectedManicure.style.display = 'block';
                }
            }
        });
    });
});

var animateElement = function(e) {
  e.preventDefault();

  var currentTarget = e.currentTarget;

  if (currentTarget) {
    currentTarget.classList.remove('animate');
    void currentTarget.offsetWidth; // Триггер рефлоу, чтобы перезапустить анимацию
    currentTarget.classList.add('animate');

    setTimeout(function(){
      currentTarget.classList.remove('animate');
    }, 700);
  }
};

var bubblyButtons = document.querySelectorAll(".bubbly-button");

for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener('click', animateElement, false);
}
