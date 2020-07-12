class Point{
	constructor (x,y,r){
		this.x=x;
		this.y=y;
		this.r=r;
		this.circle=null;
	}
	desactive(){
		let h = 0;
		noStroke();
		for (let r = this.r; r > 0; --r) {
		    fill(0,0,h*255/this.r);
		    circle(this.x, this.y, r);
		    h++;   
		}
	}
	active(){
		stroke(0);
		noFill();
		circle(this.x, this.y, this.r-2);
		fill(0);
		circle(this.x, this.y,2);
	}
	
	clicked(){
		if(dist(mouseX,mouseY,this.x,this.y)<this.r/2){
			this.active();
			return true;
		}
		this.desactive();
		return false;
	}
};



function p(val){
	console.log(val);
}