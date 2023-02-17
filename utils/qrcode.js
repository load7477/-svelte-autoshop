import QRCode from "qrcode"

function qrcodegen(amount) {
  QRCode.toString(`https://toss.me/${amount}`,{type:'terminal'}, function (err, url) {
    console.log(url)
    return url
  })
}