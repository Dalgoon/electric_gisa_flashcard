import React, { useState, useEffect, useRef } from 'react';
import classNames from 'classnames';
import { CheckCircle } from 'lucide-react';
import TextWithMath from './TextWithMath';
import './Flashcard.css';

const Flashcard = ({ card, isFlipped, setIsFlipped, isMemorized }) => {
  const [cardHeight, setCardHeight] = useState(400);
  const frontRef = useRef(null);
  const backRef = useRef(null);

  // Reset flip state when card changes
  useEffect(() => {
    setIsFlipped(false);
  }, [card, setIsFlipped]);

  // Dynamically calculate and update card height based on content
  useEffect(() => {
    const updateHeight = () => {
      if (frontRef.current && backRef.current) {
        const frontHeight = frontRef.current.scrollHeight;
        const backHeight = backRef.current.scrollHeight;
        const minHeight = window.innerWidth <= 600 ? 320 : 400;
        
        // Take the maximum height between front, back, and the baseline minimum height
        setCardHeight(Math.max(minHeight, frontHeight, backHeight));
      }
    };

    // Run measurement immediately
    updateHeight();

    // Re-run after a short delay to allow KaTeX rendering to complete
    const timer = setTimeout(updateHeight, 100);

    window.addEventListener('resize', updateHeight);
    return () => {
      clearTimeout(timer);
      window.removeEventListener('resize', updateHeight);
    };
  }, [card]);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div 
      className={classNames('flashcard-container', { 'memorized': isMemorized })}
      onClick={handleFlip}
      style={{ height: `${cardHeight}px` }}
    >
      <div className={classNames('flashcard', { 'flipped': isFlipped })}>
        
        {/* Front Face */}
        <div ref={frontRef} className="flashcard-face flashcard-front">
          <div className="card-header">
            <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
              <span className="topic-badge">{card.topic}</span>
              {card.isCustom && <span className="custom-badge">나만의 카드</span>}
            </div>
            {isMemorized && <CheckCircle size={24} color="#10b981" />}
          </div>
          <div className="card-content">
            <div>
              <TextWithMath text={card.question} />
            </div>
          </div>
          <div className="card-footer">
            Click to see the answer
          </div>
        </div>

        {/* Back Face */}
        <div ref={backRef} className="flashcard-face flashcard-back">
          <div className="card-header">
            <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
              <span className="topic-badge">Answer</span>
              {card.isCustom && <span className="custom-badge">나만의 카드</span>}
            </div>
            {isMemorized && <CheckCircle size={24} color="#10b981" />}
          </div>
          <div className="card-content">
            <div>
              <TextWithMath text={card.answer} />
            </div>
          </div>
          <div className="card-footer">
            Click to see the question
          </div>
        </div>

      </div>
    </div>
  );
};

export default Flashcard;
