function isValidTree(tree) {
    let isTreeValid = true;
    if (tree.hasOwnProperty('ornament') && tree.hasOwnProperty('color') &&
        tree.ornament == 'star' && tree.color == 'yellow') {

        if (tree.hasOwnProperty('left')) {
            treeTraversal(tree.left);
        }
        if (isTreeValid) {
            if (tree.hasOwnProperty('right')) {
                treeTraversal(tree.right);
            }
        }
    } else {
        isTreeValid = false;
    }

    function treeTraversal(treePart) {
        if (!treePart.hasOwnProperty('left') && !treePart.hasOwnProperty('right')) {
            if (treePart.color != 'blue') {
                isTreeValid = false;
            }
            return;
        } else {
            if (treePart.color != 'red') {
                isTreeValid = false;
                return;
            }
        }
        if (treePart.hasOwnProperty('left')) {
            treeTraversal(treePart.left);
        }
        if (treePart.hasOwnProperty('right')) {
            treeTraversal(treePart.right);
        }
    }

    return isTreeValid;
}

// console.log(isValidTree(
//     {
//         ornament: 'star',
//         color: 'yellow'
//     }
// ));
// console.log(isValidTree(
//     {
//         ornament: 'star',
//         color: 'yellow',
//         left: {
//             ornament: 'candy cane',
//             color: 'blue'
//         }
//     }
// ));
// console.log(isValidTree(
//     {
//         ornament: 'star',
//         color: 'yellow',
//         right: {
//             ornament: 'stocking',
//             color: 'red'
//         }
//     }
// ));
// console.log(isValidTree(
//     {
//         ornament: 'star',
//         color: 'yellow',
//         left: {
//             ornament: 'candy cane',
//             color: 'blue'
//         },
//         right: {
//             ornament: 'stocking',
//             color: 'blue'
//         }
//     }
// ));
// console.log(isValidTree(
//     {
//         ornament: 'horsey',
//         color: 'yellow',
//         left: {
//             ornament: 'candy cane',
//             color: 'blue'
//         },
//         right: {
//             ornament: 'stocking',
//             color: 'blue'
//         }
//     }
// ));