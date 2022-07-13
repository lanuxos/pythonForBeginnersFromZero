$(document).ready(function () {
    $('table.display').DataTable({
        dom: 'Bfrtlp',
        buttons: [{

                extend: 'copyHtml5',
                text: 'Copy',
                titleAttr: 'Copy',
                copySuccess: {
                    1: "Copy 1 ແຖວໄວ້ໃນ Clipboard ແລ້ວ",
                    _: "Copy %d ແຖວໄວ້ໃນ Clipboard ແລ້ວ",
                },
                copyKeys: 'ກົດປຸ່ມ <i>ctrl</i> ຫລື <i>\u2318</i> + <i>C</i> ເພື່ອ copy ຂໍ້ມູນໃນຕາຕະລາງ<br>ໄວ້ໃນ clipboard.<br><br>ຫາກຕ້ອງການຍົກເລີກກົດຂໍ້ຄວາມນີ້ ຫລື ກົດປຸ່ມ Esc.'
            },
            {
                extend: 'print',
                text: 'ສັ່ງພິມ',
                // message: 'ຕາຕະລາງລາຄາວັດຖຸ'
            },
            {
                extend: 'excelHtml5',
                text: 'Excel',
                // title: 'ຕາຕະລາງລາຄາວັດຖຸ'
            }
        ],
        "pageLength": 10,
        "lengthMenu": [
            [10, 25, 50, -1],
            [10, 25, 50, "ທັງໝົດ"]
        ],
        bLengthChange: true,
        "language": {
            "search": "ຄົ້ນຫາ:",
            "paginate": {
                "previous": "ໜ້າກ່ອນ",
                "next": "ໜ້າຖັດໄປ",
                "to": "ຫາ",
                "of": "ຈາກ",
                "entries": "ລາຍການ",
                "showing": "ສະແດງລາຍການທີ",
            },
            "decimal": "",
            "emptyTable": "ບໍ່ມີຂໍ້ມູນໃນຕາຕະລາງ",
            "info": "ສະແດງລາຍການ _START_ ຫາ _END_ ຈາກ _TOTAL_ ລາຍການ",
            "infoEmpty": "ບໍ່ພົບຂໍ້ມູນໃນຕາຕະລາງ",
            "infoFiltered": "(ຈັດລຽງຈາກ _MAX_ ຈາກລາຍການທັງໝົດ)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "ສະແດງ _MENU_ ຈາກລາຍການທັງໝົດ",
            "loadingRecords": "ກຳລັງດຶງຂໍ້ມູນມາສະແດງ...",
            "processing": "ກຳລັງປະມວນຜົນ...",
            "zeroRecords": "ບໍ່ພົບຂໍ້ມູນທີ່ກົງກັນ",
            "aria": {
                "sortAscending": ": ສະແດງແຕ່ນ້ອຍຫາໃຫຍ່",
                "sortDescending": ": ສະແດງແຕ່ໃຫຍ່ຫານ້ອຍ"
            }
        },
        columnDefs: [{
            targets: '0',
            orderable: false
        }]
    });
});