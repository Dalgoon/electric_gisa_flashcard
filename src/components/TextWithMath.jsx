import React from 'react';
import { InlineMath, BlockMath } from 'react-katex';
import 'katex/dist/katex.min.css';

/**
 * A component to render text containing $inline$ and $$block$$ math.
 */
const TextWithMath = ({ text }) => {
  if (!text) return null;

  // Split by $$ first for block math
  const blockParts = text.split(/(\$\$.*?\$\$)/gs);

  return (
    <>
      {blockParts.map((part, index) => {
        if (part.startsWith('$$') && part.endsWith('$$')) {
          const math = part.slice(2, -2);
          return <BlockMath key={index} math={math} />;
        }

        // Split remaining parts by $ for inline math
        const inlineParts = part.split(/(\$.*?\$)/g);
        
        return (
          <React.Fragment key={index}>
            {inlineParts.map((inlinePart, i) => {
              if (inlinePart.startsWith('$') && inlinePart.endsWith('$')) {
                const math = inlinePart.slice(1, -1);
                return <InlineMath key={i} math={math} />;
              }
              // Render newlines as <br />
              return (
                <span key={i}>
                  {inlinePart.split('\n').map((line, j) => (
                    <React.Fragment key={j}>
                      {line}
                      {j < inlinePart.split('\n').length - 1 && <br />}
                    </React.Fragment>
                  ))}
                </span>
              );
            })}
          </React.Fragment>
        );
      })}
    </>
  );
};

export default TextWithMath;
