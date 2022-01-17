

            '''//Remove points with y equal to y_max
            for (let i = activeCriticalPoints.length - 1; i >= 0; i--) {
                let point = activeCriticalPoints[i];
                let index = (point.index + point.dir + Line.visitedPoints.length) % Line.visitedPoints.length;
                let pMax = Line.visitedPoints[index];

                if (pMax[1] === y) activeCriticalPoints.splice(i, 1);
            }'''


            //Paint between each pair of active points
            for (let i = 0; i < activeCriticalPoints.length; i += 2) {
                let xStart = Math.round(activeCriticalPoints[i].xIntersection);
                let xEnd = Math.round(activeCriticalPoints[i + 1].xIntersection);                   

                for (let x = xStart; x < xEnd; x++) {                                       
                    let pixelColor = Canvas.getColorPixel([x, y]);

                    if (pixelColor !== colors.RED) Canvas.paintPixel([x, y], colors.GREEN, true);


