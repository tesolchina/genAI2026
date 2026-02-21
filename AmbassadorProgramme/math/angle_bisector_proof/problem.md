# Angle Bisector Symmetry Proof

**Source image:** [problem.png](problem.png)

## Problem Statement (Chinese original)

如图，\( CF \) 为 \( \angle ACB \) 的角分线。
在线段 \( AB \) 上取两点 \( D \) 和 \( E \)，使射线 \( CD \) 和 \( CE \) 关于射线 \( CF \) 对称。

求证：

$$
AC \cdot BC = \sqrt{AD \cdot DB \cdot BE \cdot EA} + CD \cdot CE
$$

**备注：** 希望尽量用构造相似三角形的办法，最好不要用到勾股定理和余弦定理。

## Problem Statement (English translation)

As shown in the figure, \( CF \) is the angle bisector of \( \angle ACB \).

On segment \( AB \), choose two points \( D \) and \( E \) such that rays \( CD \) and \( CE \) are symmetric (reflections of each other) about ray \( CF \).

**Prove that:**

$$
AC \cdot BC = \sqrt{AD \cdot DB \cdot BE \cdot EA} \;+\; CD \cdot CE
$$

**Remark:** Preferably use a method that constructs similar triangles. Avoid using the Pythagorean theorem or the law of cosines.

## Figure Description

```
            C
           /|\
          / | \
         /  |  \
        / α | α \        α = ½ ∠ACB  (CF bisects ∠ACB)
       /    |    \
      /   β | β   \      β = ∠DCF = ∠ECF  (CD, CE symmetric about CF)
     /   /  |  \   \
    /  /    |    \  \
   / /      |      \ \
  //        |        \\
 A----D---F----E-------B
```

### Geometric elements

| Element | Description |
|---------|-------------|
| \( \triangle ACB \) | The main triangle with vertex \( C \) at the top and base \( AB \) at the bottom. |
| \( CF \) | The angle bisector of \( \angle ACB \), meeting \( AB \) at foot \( F \). |
| \( D \) | A point on segment \( AB \), between \( A \) and \( F \). |
| \( E \) | A point on segment \( AB \), between \( F \) and \( B \). |
| Ray \( CD \) | From \( C \) through \( D \); symmetric to ray \( CE \) about \( CF \). |
| Ray \( CE \) | From \( C \) through \( E \); symmetric to ray \( CD \) about \( CF \). |

### Point ordering on segment AB

$$
A \;-\; D \;-\; F \;-\; E \;-\; B
$$

### Angle relationships

- \( \angle ACF = \angle BCF = \alpha \) (angle bisector)
- \( \angle DCF = \angle ECF = \beta \) (symmetry of \( CD \) and \( CE \) about \( CF \))
- Therefore \( \angle ACD = \alpha - \beta \) and \( \angle BCE = \alpha - \beta \)
- And \( \angle ACE = \alpha + \beta \) and \( \angle BCD = \alpha + \beta \)
