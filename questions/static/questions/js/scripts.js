$(document).ready(function () {
  function add_class_star(tag) {
    tag.removeClass("bi-star-fill");
    tag.addClass("bi-star");
  }

  function add_class_fill(tag) {
    tag.removeClass("bi-star");
    tag.addClass("bi-star-fill");
  }

  var answers = $(".assessments");

  function star_value(id) {
    const star1 = $("#star-1-" + id);
    const star2 = $("#star-2-" + id);
    const star3 = $("#star-3-" + id);
    const star4 = $("#star-4-" + id);
    const star5 = $("#star-5-" + id);

    var star_val = document.querySelector("#count_answer-" + id);
    star_val = parseFloat(star_val.innerHTML);

    if (star_val < 1.0) {
      add_class_star(star1);
      add_class_star(star2);
      add_class_star(star3);
      add_class_star(star4);
      add_class_star(star5);
    }

    if (star_val >= 1.0 && star_val < 2.0) {
      add_class_fill(star1);
      add_class_star(star2);
      add_class_star(star3);
      add_class_star(star4);
      add_class_star(star5);
    }

    if (star_val >= 2.0 && star_val < 3.0) {
      add_class_fill(star1);
      add_class_fill(star2);
      add_class_star(star3);
      add_class_star(star4);
      add_class_star(star5);
    }

    if (star_val >= 3.0 && star_val < 4.0) {
      add_class_fill(star1);
      add_class_fill(star2);
      add_class_fill(star3);
      add_class_star(star4);
      add_class_star(star5);
    }

    if (star_val >= 4.0 && star_val < 5.0) {
      add_class_fill(star1);
      add_class_fill(star2);
      add_class_fill(star3);
      add_class_fill(star4);
      add_class_star(star5);
    }

    if (star_val == 5.0) {
      add_class_fill(star1);
      add_class_fill(star2);
      add_class_fill(star3);
      add_class_fill(star4);
      add_class_fill(star5);
    }
  }

  answers.each(function (index) {
    var id = $(this).attr("id");

    star_value(id);

    const star1 = $("#star-1-" + id);
    const star2 = $("#star-2-" + id);
    const star3 = $("#star-3-" + id);
    const star4 = $("#star-4-" + id);
    const star5 = $("#star-5-" + id);

    const assessments = $("#assessments-" + id);
    console.log(assessments.attr("value"));

    star1.hover(
      function () {
        if (assessments.attr("value") == "False") {
          $(this).css("cursor", "pointer");
          add_class_fill(star1);
          add_class_star(star2);
          add_class_star(star3);
          add_class_star(star4);
          add_class_star(star5);
        }
      },
      function () {
        $(this).css("cursor", "auto");
        star_value(id);
      }
    );

    star2.hover(
      function () {
        if (assessments.attr("value") == "False") {
          $(this).css("cursor", "pointer");
          add_class_fill(star1);
          add_class_fill(star2);
          add_class_star(star3);
          add_class_star(star4);
          add_class_star(star5);
        }
      },
      function () {
        $(this).css("cursor", "auto");
        star_value(id);
      }
    );

    star3.hover(
      function () {
        if (assessments.attr("value") == "False") {
          $(this).css("cursor", "pointer");
          add_class_fill(star1);
          add_class_fill(star2);
          add_class_fill(star3);
          add_class_star(star4);
          add_class_star(star5);
        }
      },
      function () {
        $(this).css("cursor", "auto");
        star_value(id);
      }
    );

    star4.hover(
      function () {
        if (assessments.attr("value") == "False") {
          $(this).css("cursor", "pointer");
          add_class_fill(star1);
          add_class_fill(star2);
          add_class_fill(star3);
          add_class_fill(star4);
          add_class_star(star5);
        }
      },
      function () {
        $(this).css("cursor", "auto");
        star_value(id);
      }
    );

    star5.hover(
      function () {
        if (assessments.attr("value") == "False") {
          $(this).css("cursor", "pointer");
          add_class_fill(star1);
          add_class_fill(star2);
          add_class_fill(star3);
          add_class_fill(star4);
          add_class_fill(star5);
        }
      },
      function () {
        star_value(id);
      }
    );

    var value_likes = $("#answers-likes-" + id);

    value_likes.hover(
      function () {
        if (value_likes.attr("value") == "none") {
          $(this).css("background-color", "#FFEFED");
          $(this).css("cursor", "pointer");
        }
      },
      function () {
        $(this).css("background-color", "transparent");
        $(this).css("cursor", "auto");
      }
    );
  });

  $(".textarea")
    .each(function () {
      this.setAttribute(
        "style",
        "height:" + this.scrollHeight + "px;overflow-y:hidden;"
      );
    })
    .on("input", function () {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    });
});
