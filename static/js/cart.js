
var updateBtns=document.getElementsByClassName('update-cart')

for(var i=0; i< updateBtns.length; i++){
	updateBtns[i].addEventListener('click',function(){
		var productId= this.dataset.product
		var action= this.dataset.action
		
		value=document.getElementById('quant').value
		size=document.getElementById('size').value

		console.log("productId:",productId, "action:",action)
		console.log('USER:',user)
		console.log('quanti:',value)
		if (user ==='AnonymousUser'){
			console.log('Not logged in')
		}else{
			updateUserOrder(productId,action,value,size)
		}


		
	})
}


function updateUserOrder(productId,action,quant,size){
	console.log('user is logged in sending data..')

	var url = '/update_item/'

	fetch(url,{
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'productId':productId,'action':action,'quant':quant,'size':size})
	})

	.then((response) =>{
		return response.json()
	})

	.then((data) => {
		console.log('data:',data)
		location.reload()
	})

}

