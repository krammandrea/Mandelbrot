//a couple of helpers for main.html of the Mandelbrot project
var MBMAINHELPERS = {

    hideShowBlock: function (block){
	if (block.style.display=="block"){
	    block.style.display="none";
	}
	else{
	    block.style.display="block";
	}
    },

    //checks to user input for disallowed characters and a maximum size and pops
    //up a warning and the instruction to try again
    validateSizeInput: function(sizeForm){
	//option:flexible maxSize?
	var regExpOnlyNumbers = new RegExp("^[1-9]{1}[0-9]{0,5}$"); 
	//all numbers from 1-999999
	if( sizeForm.imagewidth.value=="" ||
	    sizeForm.imageheight.value==""||
	    !regExpOnlyNumbers.test(sizeForm.imagewidth.value) ||
	    !regExpOnlyNumbers.test(sizeForm.imageheight.value)){
            alert("Please choose both the width and the height of the picture, using values from 1-999999")
	    //alternative: red text beside the boxes
            sizeForm.imagewidth.focus();
            return false;
	}
	return true;	
    },

    validateIterationInput: function(iterationForm){
	var regExpOnlyNumbers = new RegExp("^[1-9]{1}[0-9]{0,3}$");
	//all numbers from 1-9999
	if (iterationForm.iteration.value=="" ||
	    !regExpOnlyNumbers.test(iterationForm.iteration.value)){
	    alert("Please choose an iteration value from 1-9999");
	    return false;
	}; 
	return true;
    },	    

    validateColorInput: function(colorForm){
	var regExpOnlyHex = new RegExp("^([0-9a-fA-F]{3}){1,2}$");
	//only hexnumbers 3 or 6 numbers long
	if( colorForm.first_color.value=="" ||
	    !regExpOnlyHex.test(colorForm.first_color.value)){
	    alert("Please choose a hexadezimal number with values from 0 to F");
	    return false;
	};
	var secondaryColors = MBMAINHELPERS.findSecondaryColorsNodes();
	for (var    currentColor = 0; 
		    currentColor < secondaryColors.length; 
		    currentColor ++){
	    if( secondaryColors[currentColor].children[1].value=="" ||
		!regExpOnlyHex.test(secondaryColors[currentColor].children[1].value)){
		alert("Please choose a hexadezimal number with values from 0 to F");
		return false;
	    };
	};
	return true;
    },

    findSecondaryColorsNodes: function(){
	//find all the color_blocks in the secondory color section
	var colorPickers = document.getElementById("color_pickers_form_secondary_colors");
	var secondaryColors = new Array();
	for (node=0; node < colorPickers.childNodes.length;node++){
	    if(colorPickers.childNodes[node].className === "color_block"){
		secondaryColors.push(colorPickers.childNodes[node]);
	    };
	};
	return secondaryColors;
    },


    addColor: function (currentNode){
	var inputElement = MBMAINHELPERS.findSecondaryColorsNodes()[0].cloneNode(true);
	// bind jscolor
	var colorElement = new jscolor.color(inputElement.children[1]);
	colorElement.fromString('F2C80A');

	//add the new element at the buttom 
	document.getElementById('color_pickers_form_secondary_colors').insertBefore(inputElement,currentNode.nextSibling);

	var oldHeight = document.getElementById('rotate_button').offsetHeight;
	var newHeight = String(oldHeight + 26);
	document.getElementById('rotate_button').style.height = newHeight;
    },


    removeColor:function(currentNode){
	//check for a minimum of 2 colors
	var numberOfColors = 0;
	var color_pickers = document.getElementById("color_pickers_form_secondary_colors");
	for (node=0; node < color_pickers.childNodes.length;node++){
	    if(color_pickers.childNodes[node].className === "color_block"){
		numberOfColors +=1;
		};
	    };
	if (numberOfColors>2){
	    var last_element = color_pickers.lastChild;
	    color_pickers.removeChild(currentNode);

	    var oldHeight = document.getElementById('rotate_button').offsetHeight;
	    var newHeight = String(oldHeight - 26);
	    document.getElementById('rotate_button').style.height = newHeight;
	    };
	},


    rotateColors:function(){
	//rotate the succession of the colors, all but the first
	var color_pickers = document.getElementById("color_pickers_form_secondary_colors");
	var second_color = MBMAINHELPERS.findSecondaryColorsNodes()[0];
	var last_color= color_pickers.lastChild;
	color_pickers.insertBefore(last_color,second_color);
    },


    calculatingImageEffect:function(image,progressbar){
	    progressbar.style.display="inline";
	    image.style.opacity="0.5";
	    }
}
