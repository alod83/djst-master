$(document).ready(function(){
  // Aggiunge l'effetto a tutti i link
       
  $("a").on('click', function(event) {
 
    // Controlla che hash abbia un valore
    if (this.hash !== "") {
		
      event.preventDefault();

      var hash = this.hash;

      // Usa jQuery's animate() per aggiungere l'effetto smooth
      // Il numero (850) specifica il numero di millisecondi presi per scorrere l'area specificata
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1500, function(){
   
        // Aggiunge (#) all URL quando si scorre
		window.location.hash = hash;

        
      });
    } 
  });
});