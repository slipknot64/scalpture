function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
        end = dc.length;
        }
    }
    return decodeURI(dc.substring(begin + prefix.length, end));
} 

function tos_check() {
    var tos = getCookie("tos-accept");
    if (tos == null) {
        consent();
    }
    else {

    }
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function consent() {
    var r = window.confirm("By using this website and closing this notification, I accept to adheer to the following points:\n- I am using this receipt to test my-company/customer-service / a-company-im-working-for / a-service-agreed-by-said-company.\n- That this service is available for EDUCATIONAL PURPOSES ONLY.\n- That I (You, the user) will be held responsible for any documents/receipts that are used in any illicit way. Receipt Mansion DOES NOT condone any illegal activities.\nThank you & have a nice day!\n~ Receipt Mansion~\n");
    if (r == true) {
        setCookie("tos-accept","yes",1);
    } else {
        window.history.go(-1); return false;
    }
}

// Amazon 3rd Party Check

document.getElementById("input_amazon3rdparty").onclick = function(){
    if (document.getElementById('input_amazon3rdparty').checked) {
        document.getElementById('amazoninvoice_3rdparty').style.display='';
        document.getElementById('AmazonInvoiceForm').action='/modules/Amazon/amazoninvoice3rdparty.php';
    } else {
        document.getElementById('amazoninvoice_3rdparty').style.display='none';
        document.getElementById('AmazonInvoiceForm').action='/modules/Amazon/amazoninvoice.php';
    }    
}

document.getElementById("input_newegg").onclick = function(){
    if (document.getElementById('input_newegg').checked) {
        document.getElementById('newegg_address2').style.display='';
    } else {
        document.getElementById('newegg_address2').style.display='none';
    }    
}
