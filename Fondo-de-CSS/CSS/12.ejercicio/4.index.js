var modal = $('#modal');

$(function(){
  $('img').click(function(){
    var idImg = $(this).attr("id");
    console.log(idImg)
    var srcImg = $(this).attr("src");
    console.log(srcImg);
    showModal(idImg,srcImg);
  });
  hideModal();
});

function showModal(idImg,srcImg){
    var imagen = idImg;
    var src = srcImg;
    $('#imgModal').attr("src",srcImg);
    modal.css("display", "block");
  }
  function hideModal() {
    $('.cerrar').click(function(){
      modal.css("display", "none");
    });
  }