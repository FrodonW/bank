$(document).ready(function () {

var endpoint = $("#js-products").attr("data-url");
$.ajax({
    method: 'GET',
    url: endpoint,
    success: function (data) {
        console.log(data['data'])
        var table = new Tabulator("#bodyTable", {
            data: data['data'], //assign data to table
            autoColumns:true, //create columns from data field names
        });



    },
    error: function (error_data) {
        console.log(error_data)
    }
})
})