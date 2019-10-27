$('#create_product').click(function(e){
  e.preventDefault()
  alert('clicked');
  $.ajax({
        url : "/ecommerce/product/", // the endpoint
        type : "POST", // http method
        headers: {
                    'X-CSRF-Token': $('#csrf_token').val()
               },
        data : {
          name : $('#product_name').val(),
          description: $('#product_description').val(),
          price: $('#price').val(),
          slug: $('#slug').val()


        }, // data sent with the post request

        // handle a successful response
        success : function(json) {

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

        }
    });
  console.log('form',$('product_form').serialize()) //this produces: "foo=1&bar=xxx&this=hi"

});
