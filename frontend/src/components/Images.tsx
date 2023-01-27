import React from "react";
import "./index.css";
import { Context } from "./SearchEngine";

function Images({ images }: { images: any[] }) {
  return (
    <div className="images-wrapper">
      {images.map((imgData) => {
        return (
          <div className="img-wrapper">
            <img className="img-res" src={imgData.payload.image_url} />
                        {imgData?.payload?.metadata ? (
              <p className="similarity-checksum">{imgData.payload.metadata}</p>
            ) : (
              <></>
            )}

            {imgData?.score ? (
              <p className="similarity-checksum">Similarity: {imgData.score}</p>
            ) : (
              <></>
            )}

          </div>
        );
      })}
    </div>
  );
}

export default Images;
