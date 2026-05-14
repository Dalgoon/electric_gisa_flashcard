import React, { useState, useEffect } from 'react';
import { ArrowLeft, ArrowRight, Shuffle, CheckCircle, RotateCcw } from 'lucide-react';
import Flashcard from './Flashcard';
import './Deck.css';

const Deck = ({ cards, excludeMemorized }) => {
  const [currentCards, setCurrentCards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [touchStart, setTouchStart] = useState(null);
  const [touchEnd, setTouchEnd] = useState(null);
  const [slideDirection, setSlideDirection] = useState(null);
  const [isAnimating, setIsAnimating] = useState(false);
  const [memorizedIds, setMemorizedIds] = useState(() => {
    try {
      const saved = localStorage.getItem('memorizedIds');
      if (saved) return new Set(JSON.parse(saved));
    } catch (e) {
      console.error('Failed to load memorized cards', e);
    }
    return new Set();
  });

  useEffect(() => {
    try {
      localStorage.setItem('memorizedIds', JSON.stringify(Array.from(memorizedIds)));
    } catch (e) {
      console.error('Failed to save memorized cards', e);
    }
  }, [memorizedIds]);

  const prevCardsRef = React.useRef(cards);
  const prevExcludeRef = React.useRef(excludeMemorized);

  // Initialize and filter cards based on props
  useEffect(() => {
    let filtered = cards;
    if (excludeMemorized) {
      filtered = cards.filter(card => !memorizedIds.has(card.id));
    }
    setCurrentCards(filtered);
    
    // If cards or excludeMemorized changed, reset index to 0
    if (prevCardsRef.current !== cards || prevExcludeRef.current !== excludeMemorized) {
      setCurrentIndex(0);
      prevCardsRef.current = cards;
      prevExcludeRef.current = excludeMemorized;
    } else {
      // If only memorizedIds changed, keep the index (bound by new length)
      setCurrentIndex(prev => {
        if (filtered.length === 0) return 0;
        return Math.min(prev, filtered.length - 1);
      });
    }
  }, [cards, excludeMemorized, memorizedIds]);

  const animateToNextCard = (nextIndexFn, direction) => {
    if (isAnimating) return;
    setIsAnimating(true);
    setIsFlipped(false);
    
    // Slide out current card
    setSlideDirection(`slide-out-${direction}`);
    
    setTimeout(() => {
      // Change card index
      nextIndexFn();
      
      // Prepare for slide in
      const opposite = direction === 'left' ? 'right' : 'left';
      setSlideDirection(`slide-in-${opposite}`);
      
      // Start sliding in
      setTimeout(() => {
        setSlideDirection(null); // Removes transform to slide into center
        
        // Finish animation
        setTimeout(() => {
          setIsAnimating(false);
        }, 250);
      }, 50); // small delay to allow DOM to register the slide-in class
    }, 250);
  };

  const handleNext = () => {
    if (currentIndex < currentCards.length - 1 && !isAnimating) {
      animateToNextCard(() => setCurrentIndex(prev => prev + 1), 'left');
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0 && !isAnimating) {
      animateToNextCard(() => setCurrentIndex(prev => prev - 1), 'right');
    }
  };

  const handleShuffle = () => {
    const shuffled = [...currentCards].sort(() => Math.random() - 0.5);
    setCurrentCards(shuffled);
    setCurrentIndex(0);
  };
  
  const resetDeck = () => {
    setCurrentIndex(0);
  };

  // Swipe Handlers
  const minSwipeDistance = 50;

  const onTouchStart = (e) => {
    setTouchEnd(null);
    setTouchStart(e.targetTouches[0].clientX);
  };

  const onTouchMove = (e) => {
    setTouchEnd(e.targetTouches[0].clientX);
  };

  const onTouchEndHandler = () => {
    if (!touchStart || !touchEnd) return;
    
    const distance = touchStart - touchEnd;
    const isLeftSwipe = distance > minSwipeDistance;
    const isRightSwipe = distance < -minSwipeDistance;
    
    if (isLeftSwipe) {
      handleNext();
    }
    if (isRightSwipe) {
      handlePrev();
    }
    setTouchStart(null);
    setTouchEnd(null);
  };

  // Mouse Swipe Handlers
  const onMouseDown = (e) => {
    setTouchEnd(null);
    setTouchStart(e.clientX);
  };

  const onMouseMove = (e) => {
    if (e.buttons === 1 && touchStart !== null) { // Only track if mouse is clicked down
      setTouchEnd(e.clientX);
    }
  };

  const onMouseUp = () => {
    if (touchStart !== null && touchEnd !== null) {
      onTouchEndHandler();
    }
  };
  
  const onMouseLeave = () => {
    if (touchStart !== null && touchEnd !== null) {
      onTouchEndHandler();
    } else {
      setTouchStart(null);
      setTouchEnd(null);
    }
  };

  const toggleMemorized = () => {
    if (currentCards.length === 0) return;
    
    const currentCard = currentCards[currentIndex];
    setMemorizedIds(prev => {
      const newSet = new Set(prev);
      if (newSet.has(currentCard.id)) {
        newSet.delete(currentCard.id);
      } else {
        newSet.add(currentCard.id);
      }
      return newSet;
    });
  };

  const resetMemorized = () => {
    setMemorizedIds(new Set());
  };

  if (currentCards.length === 0) {
    return (
      <div className="empty-state">
        <h3>All caught up! 🎉</h3>
        <p>You have memorized all cards in this selection.</p>
        <button onClick={resetMemorized} className="btn">
          <RotateCcw size={18} />
          Reset Memorized Status
        </button>
      </div>
    );
  }

  const currentCard = currentCards[currentIndex];
  const isCurrentMemorized = memorizedIds.has(currentCard.id);
  const progress = ((currentIndex + 1) / currentCards.length) * 100;

  return (
    <div className="deck-container">
      <div className="progress-container">
        <div className="progress-text">
          {currentIndex + 1} / {currentCards.length}
        </div>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${progress}%` }}></div>
        </div>
      </div>

      <div 
        onTouchStart={onTouchStart}
        onTouchMove={onTouchMove}
        onTouchEnd={onTouchEndHandler}
        onMouseDown={onMouseDown}
        onMouseMove={onMouseMove}
        onMouseUp={onMouseUp}
        onMouseLeave={onMouseLeave}
        className={`swipe-wrapper ${slideDirection ? `anim-${slideDirection}` : ''}`}
        style={{ width: '100%', userSelect: 'none', cursor: 'grab' }}
      >
        <Flashcard 
          card={currentCard} 
          isFlipped={isFlipped} 
          setIsFlipped={setIsFlipped}
          isMemorized={isCurrentMemorized}
        />
      </div>

      <div className="deck-controls">
        <button 
          className="btn-icon" 
          onClick={handlePrev} 
          disabled={currentIndex === 0}
          aria-label="Previous card"
        >
          <ArrowLeft size={24} />
        </button>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button 
            className={`btn btn-outline ${isCurrentMemorized ? 'memorized-btn' : ''}`}
            onClick={toggleMemorized}
            style={{ borderColor: isCurrentMemorized ? 'var(--success-color)' : '', color: isCurrentMemorized ? 'var(--success-color)' : '' }}
          >
            <CheckCircle size={20} />
            {isCurrentMemorized ? 'Memorized' : 'Mark as Memorized'}
          </button>
          <button className="btn btn-outline" onClick={handleShuffle}>
            <Shuffle size={20} />
            Shuffle
          </button>
        </div>

        <button 
          className="btn-icon" 
          onClick={handleNext} 
          disabled={currentIndex === currentCards.length - 1}
          aria-label="Next card"
        >
          <ArrowRight size={24} />
        </button>
      </div>
    </div>
  );
};

export default Deck;
