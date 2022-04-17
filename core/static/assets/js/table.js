$(document).ready(function () {
var endpoint = $("#js-products").attr("data-url");
// var printIcon = function(cell, formatterParams){ //plain text value
//     return "<i class='fa fa-print'></i>";
// };
let btncallback = function ( e, cell) {
    console.log( cell.getData() );
};

let btn = function( value, data, cell, row, options ) {
    return `<button type="button" class="btn btn-sm btn-secondary">test</button>`;
};
$.ajax({
    method: 'GET',
    url: endpoint,
    success: function (data) {
        console.log(data['data'])
        var table = new Tabulator("#bodyTable", {
            data: data['data'], //assign data to table
            columnDefaults:{
                tooltip:function(cell){
                    //cell - cell component

                    //function should return a string for the tooltip of false to hide the tooltip
                    return  cell.getValue(); //return cells "field - value";
                },
            },
            groupBy:"id",
            layout:"fitColumns",
            resizableRows:false,
            pagination:"local",
            paginationSize:7,
            columns:[                 //define the table columns
        {title:"First name", field:"user__first_name", resizable:false},
        {title:"Last name", field:"user__last_name", resizable:false},
        {title:"Birthday", field:"birthday", formatter:"datetime", formatterParams:{
                                                                                    inputFormat:"yyyy-MM-dd",
                                                                                    outputFormat:"dd/MM/yy",
                                                                                    invalidPlaceholder:"(invalid date)",
                                                                                    timezone:"America/Los_Angeles",
        }, resizable:false},
        {title:"Gender", field:"gender", formatter:"lookup", formatterParams:{
                                                                            "1": "Mate",
                                                                            "2": "Female",
                                                                        }, resizable:false},
        {title:"Phone", field:"phone"},
        {title:"Address", field:"address", headerTooltip:true},
        {title:"City", field:"city"},
        {title:"Accept", field:"loan__loanaccept__accept", hozAlign:"center", formatter:"tickCross", formatterParams:{
                                                                            allowEmpty:true,
                                                                            allowTruthy:true,
                                                                            tickElement:"<i class='fa fa-check'></i>",
                                                                            crossElement:"<i class='fa fa-times'></i>",
            }, resizable:false},
        {title:"Action", formatter: btn, cellClick: btncallback},
    ],
        });



    },
    error: function (error_data) {
        console.log(error_data)
    }
})
})