class Point{
	constructor (x,y,r){
		this.x=x;
		this.y=y;
		this.r=r;
	}
	draw(){
		fill(255, 255, 255);
		circle(this.x,this.y,this.r);

	}
	active(){

	}
	desactive(){

	}
	clicked(){
		
		if(dist(mouseX,mouseY,this.x,this.y)<this.r/2){
			this.y=mouseY;
			this.x=mouseX;
		}
		//console.log(mouseX,mouseY);
	}
};