$(document).ready(function () {
var endpoint = $("#js-products").attr("data-url");
// var printIcon = function(cell, formatterParams){ //plain text value
//     return "<i class='fa fa-print'></i>";
// };
let btncallback = function ( e, cell) {
    console.log( cell.getData() );
};

let btn = function( value, data, cell, row, options ) {
    return `<button type="button" class="btn btn-sm btn-secondary">
            <nav class="navbar navbar-expand-sm bg-light">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="http://127.0.0.1:8000/customers/profile/">test</a>
                    </li>
                </ul>
            </nav>
            </button>`;
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
            layout:"fitColumns",
            resizableRows:false,
            pagination:"local",
            paginationSize:7,
            columns:[                 //define the table columns
                {title:"Id", field:"id", resizable:false, width:50},
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
                {title:"Phone", field:"phone", resizable:false},
                {title:"Address", field:"address", headerTooltip:true, resizable:false},
                {title:"City", field:"city", resizable:false},
                {title:"Action", formatter: btn, cellClick: btncallback, resizable:false, width:80},
            ],
                });



    },
    error: function (error_data) {
        console.log(error_data)
    }
})
})